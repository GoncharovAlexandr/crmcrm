<template>
  <div class="dashboard">
    <div class="sidebar">
      <div class="task-status">
        <div class="task-status-item">
          <div class="task-status-circle active"></div>
          <div class="task-status-label orange-text">Активные задачи ({{ activeTasks }})</div>
        </div>
        <div class="task-status-item">
          <div class="task-status-circle completed"></div>
          <div class="task-status-label grey-text">Выполненные задачи ({{ completedTasks }})</div>
        </div>
        <div class="task-status-item">
          <div class="task-status-circle overdue"></div>
          <div class="task-status-label black-text">Просроченные задачи ({{ overdueTasks }})</div>
        </div>
      </div>
    </div>
    <div class="chart-container">
      <div class="chart" :style="chartStyle"></div>
      <div class="efficiency" :class="efficiencyColor">
        <div class="efficiency-text">
          Эффективность сотрудника:
          <span class="efficiency-value">{{ efficiency.toFixed(2) }}</span>%
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      activeTasks: 30, // Замените это значение на актуальное количество активных задач
      completedTasks: 40, // Замените это значение на актуальное количество выполненных задач
      overdueTasks: 1, // Замените это значение на актуальное количество просроченных задач
    };
  },
  computed: {
    chartStyle() {
      const totalTasks = this.activeTasks + this.completedTasks + this.overdueTasks;
      const activePercentage = (this.activeTasks / totalTasks) * 100;
      const completedPercentage = (this.completedTasks / totalTasks) * 100;
      const overduePercentage = (this.overdueTasks / totalTasks) * 100;

      return `
        background-image: conic-gradient(
          var(--active-color, #ff9900) 0deg ${activePercentage}%,
          var(--completed-color, #828282) ${activePercentage}% ${activePercentage + completedPercentage}%,
          var(--overdue-color, #000000) ${activePercentage + completedPercentage}% 100%
        );
        width: 400px;
        height: 400px;
      `;
    },
    efficiency() {
      const totalTasks = this.completedTasks + this.activeTasks + this.overdueTasks;
      const completedPercentage = (this.completedTasks / totalTasks) * 100;
      return completedPercentage;
    },
    efficiencyColor() {
      if (this.efficiency > 80) {
        return 'grey';
      } else if (this.efficiency > 50) {
        return 'orange';
      } else {
        return 'black';
      }
    },
  },
};
</script>
<style>
.task-status {
  display: flex;
  flex-direction: column;
}

.task-status-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.task-status-circle {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  margin-right: 10px;
}

.task-status-label {
  color: #fff;
}

.active {
  background-color: var(--active-color, #ff9900);
}

.completed {
  background-color: var(--completed-color, #828282);
}

.overdue {
  background-color: var(--overdue-color, #000000);
}

.chart {
  width: 400px;
  height: 400px;
  border-radius: 50%;
  margin: 0 auto;
}

.efficiency {
  margin-top: 20px;
  padding: 10px;
  text-align: center;
}

.efficiency.grey {
  background-color: grey;
  color: #fff;
}

.efficiency.orange {
  background-color: orange;
  color: #fff;
}

.efficiency.black {
  background-color: black;
  color: #fff;
}

.efficiency-value {
  font-weight: bold;
  margin-left: 5px;
}
</style>