<template>
  <div class="HistoriaClinica">
    <div class="container_izquierda">
      <InterfazUsuario></InterfazUsuario>
      <Menu></Menu>
    </div>
    
    <historiaClinica></historiaClinica>
  </div>
</template>

<script>
import InterfazUsuario from '../components/InterfazUsuario.vue'
import Menu from '../components/Menu.vue'
import HistoriaClinica from '../components/interfazHistoriaClinica.vue'

export default {
  components:{
    InterfazUsuario,
    Menu,
    HistoriaClinica
  }
}
</script>

<style>
.container_izquierda{
  width: 35%;
  display: inline-block;
}
</style>