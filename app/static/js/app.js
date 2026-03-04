document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('taskForm');
    const taskList = document.getElementById('taskList');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const sortSelect = document.getElementById('sortSelect');

    let currentFilter = 'all';

    // Fetch and render tasks
    async function fetchTasks() {
        const sort = sortSelect.value;
        const response = await fetch(`/api/tasks?sort=${sort}`);
        const tasks = await response.json();
        renderTasks(tasks);
    }

    function renderTasks(tasks) {
        taskList.innerHTML = '';
        
        const filteredTasks = tasks.filter(task => {
            if (currentFilter === 'active') return !task.completed;
            if (currentFilter === 'completed') return task.completed;
            return true;
        });

        filteredTasks.forEach(task => {
            const card = document.createElement('div');
            card.className = 'task-card';
            if (task.completed) card.style.opacity = '0.7';

            const dueDate = task.due_date ? new Date(task.due_date).toLocaleDateString() : 'Pas de date';
            
            card.innerHTML = `
                <div class="task-info">
                    <div class="checkbox ${task.completed ? 'completed' : ''}" onclick="toggleTask(${task.id}, ${task.completed})"></div>
                    <div class="task-text">
                        <div class="task-title ${task.completed ? 'completed' : ''}">${task.title}</div>
                        <div class="task-meta">
                            <span class="priority-badge priority-${task.priority.toLowerCase()}">${task.priority}</span>
                            <span>📅 ${dueDate}</span>
                        </div>
                    </div>
                </div>
                <div class="task-actions">
                    <button class="btn-delete" onclick="deleteTask(${task.id})">🗑️</button>
                </div>
            `;
            taskList.appendChild(card);
        });
    }

    // Create Task
    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const data = {
            title: document.getElementById('title').value,
            description: document.getElementById('description').value,
            priority: document.getElementById('priority').value,
            due_date: document.getElementById('dueDate').value || null
        };

        const response = await fetch('/api/tasks', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            taskForm.reset();
            fetchTasks();
        }
    });

    // Toggle Complete
    window.toggleTask = async (id, currentStatus) => {
        await fetch(`/api/tasks/${id}`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ completed: !currentStatus })
        });
        fetchTasks();
    };

    // Delete Task
    window.deleteTask = async (id) => {
        if (confirm('Supprimer cette tâche ?')) {
            await fetch(`/api/tasks/${id}`, { method: 'DELETE' });
            fetchTasks();
        }
    };

    // Filters
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentFilter = btn.dataset.filter;
            fetchTasks();
        });
    });

    sortSelect.addEventListener('change', fetchTasks);

    // Initial Load
    fetchTasks();
});
