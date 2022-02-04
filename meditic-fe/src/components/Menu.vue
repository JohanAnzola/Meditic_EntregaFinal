<template>
  <div class= 'menu_container'>
    <div>
      <img class="iconCalendario" src="../assets/iconCalendario.png">
      <h2 class="calendario_texto">Calendario</h2>
    </div>
    <div>
      <img class="iconCarpeta" src="../assets/iconCarpeta.png">
      <h2 class="historiasClinicas_texto">Historia Clinica</h2>
    </div>
    <div>
      <img class="iconConfiguracion" src="../assets/iconConfiguracion.png">
      <h2 class="configuracion_texto">Configuracion</h2>
    </div>
    <div>
      <img class="iconCerrarSesion" src="../assets/iconCerrarSesion.png">
      <h2 class="cerrarSesion_texto">Cerrar Sesion</h2>
    </div>  
  </div>
</template>

<script>
export default {
  name: 'Menu',
  props: {

  }
}
</script>

<style>
.menu_container{
  margin: 20px;
  border: black 3px solid;
  height: 33em;  
}
.iconCalendario{
  display: inline-block;
  width: 4em;
  height: 4em;
  margin-left: 10px;
  margin-top:10px
}
.calendario_texto{
  display: inline-block;
  position: relative;
  font-size: 1,5em;
  margin:5px;
  left:10px;
  bottom: 30px;
}

.iconCarpeta{
  display: inline-block;
  width: 4em;
  height: 4em;
  margin-left: 10px;
  margin-top:10px
}
.historiasClinicas_texto{
  display: inline-block;
  position: relative;
  font-size: 1,5em;
  margin:5px;
  left:10px;
  bottom: 30px;
}

.iconConfiguracion{
  display: inline-block;
  width: 4em;
  height: 4em;
  margin-left: 10px;
  margin-top:10px
}
.configuracion_texto{
  display: inline-block;
  position: relative;
  font-size: 1,5em;
  margin:5px;
  left:10px;
  bottom: 30px;
}

.iconCerrarSesion{
  display: inline-block;
  width: 4em;
  height: 4em;
  margin-left: 10px;
  margin-top:10px
}
.cerrarSesion_texto{
  display: inline-block;
  position: relative;
  font-size: 1,5em;
  margin:5px;
  left:10px;
  bottom: 30px;
}

</style>