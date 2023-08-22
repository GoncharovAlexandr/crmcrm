<template>
  <form class="card auth-card" @submit.prevent="submitHandler">
    <div class="card-content">
      <span class="card-title">Войти в аккаунт:</span>
      <div class="input-field">
        <input
            id="username"
            type="text"
            class="validate"
            v-model="username"
        >
        <label for="username">Имя пользователя</label>
        <small class="helper-text invalid" v-if="!username">Поле обязательно для заполнения</small>
      </div>
      <div class="input-field">
        <input
            id="password"
            type="password"
            class="validate"
            v-model="password"
        >
        <label for="password">Пароль</label>
        <small class="helper-text invalid" v-if="!password">Поле обязательно для заполнения</small>
      </div>
    </div>
    <div class="card-action">
      <div>
        <button
            class="btn waves-effect orange auth-submit"
            type="submit"
            :disabled="!username || !password"
        >
          Войти
        </button>
      </div>
      <p class="center">
        Нет аккаунта?
        <router-link to="/register">Зарегистрироваться</router-link>
      </p>
    </div>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  name: 'login',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    submitHandler() {
      if (!this.username || !this.password) {
        // Предупреждение о незаполненных полях
        alert('Пожалуйста, заполните все поля');
        return;
      }

      // Отправка запроса на сервер для аутентификации
      axios
          .post('/login/', {
            username: this.username,
            password: this.password,
          })
          .then(() => {
            // Аутентификация прошла успешно
            this.$router.push('/dashboard');
          })
          .catch((error) => {
            // Обработка ошибки аутентификации
            console.error('Ошибка аутентификации:', error);
            alert('Ошибка аутентификации');
          });
    },
  },
  created() {
    // Проверка на наличие активной сессии пользователя
    axios
        .get('/check_session/')
        .then(() => {
          // Пользователь уже аутентифицирован
          this.$router.push('/dashboard');
        })
        .catch(() => {
          // Пользователь не аутентифицирован
        });
  },
};
</script>

<style>
/* Стили для вашей формы */
</style>
