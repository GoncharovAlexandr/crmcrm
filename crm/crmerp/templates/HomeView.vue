<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logotip.png">
    <HelloWorld msg="CRM система Компьютерный мир"/>
  </div>
  <div class="card-action">
    <div>
      <button class="btn waves-effect orange auth-submit white-text" type="submit" style="height:36px;width:452px">
        <router-link to="/login">Войти</router-link>
      </button>
    </div>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
