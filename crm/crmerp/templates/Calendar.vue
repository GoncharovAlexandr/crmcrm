<template>
  <div>
    <h2>Календарь с заданиями</h2>
    <full-calendar :options="calendarOptions"></full-calendar>
  </div>
</template>

<script>
import Vue from 'vue';
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';

export default {
  components: {
    FullCalendar,
  },
  data() {
    return {
      calendarOptions: {
        plugins: [dayGridPlugin],
        initialView: 'dayGridMonth',
        events: [
          // Здесь можно добавить задания/события для отображения на календаре
          { title: 'Задание 1', start: '2023-07-01' },
          { title: 'Задание 2', start: '2023-07-05', end: '2023-07-07' },
          { title: 'Задание 3', start: '2023-07-10', allDay: true },
        ],
      },
    };
  },
};
</script>
