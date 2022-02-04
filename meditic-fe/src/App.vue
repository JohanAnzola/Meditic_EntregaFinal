<template>
  <div id="app" class="app">
    <div class="header">
      <div class = "logo">
        <img src = ./assets/logoAplicacion.svg>
        <h1>MediTic IPS</h1>
      </div>
      

      <nav>
      <button v-if="is_auth" v-on:click="loadCrearHistoria">Crear Historia Clinica</button>
        <button v-if="is_auth" v-on:click="loadHome">Historias clinicas</button>
        <button v-if="is_auth" v-on:click="logOut">Cerrar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadSignUp" > Registrarse </button>
      </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
         v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
        v-on:loadHome="loadHome"
      >
      </router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",

  data: function() {
    return {
      is_auth: localStorage.getItem("isAuth") || false,
    };
  },

  components: {},

  methods: {
    verifyAuth: function() {
      this.is_auth = localStorage.getItem("isAuth") || false;
 
      if (this.is_auth == false)
        this.$router.push({ name: "logIn" });
      else
        this.$router.push({ name: "historias_clinicas" });
    },

    loadLogIn: function() {
      this.$router.push({ name: "logIn" });
    },
       loadSignUp: function(){
      this.$router.push({name: "signUp"})
    },

    completedLogIn: function(data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.ccMedico);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      this.verifyAuth();
    },
completedSignUp: function(data) {
			alert("Registro Exitoso");
			this.completedLogIn(data);
    },
    created: function() {
      this.verifyAuth();
    },

    loadHome: function() {
      this.$router.push({ name: "historias_clinicas" });
    },

    loadCrearHistoria: function(){
      
      this.$router.push({ name: "crear_historia" });
    },

    logOut: function() {
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
    },
  },
};
</script>

<style>
body {
  margin: 0 0 0 0;
}

.header {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;

  background-color: #4E93D0;
  color: #e5e7e9;
  border: 2px solid black;

  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 120px;
  margin: 10px 20px;
}

.logo img {
  height: 4rem;
  width: 4rem;
}

.logo h1 {
  width: 50%;
  text-align: center;
}

.header h1 {
  width: 20%;
  text-align: center;
}

.header nav {
  height: 100%;
  width: 32%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}
.header nav button {
  color: #e5e7e9;
  background: #4E93D0;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 10px 20px;
}

.header nav button:hover {
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
  color: black;
}

.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;

  background: #fdfefe;
}
</style>
