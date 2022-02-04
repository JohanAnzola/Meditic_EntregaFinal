<template>
  <div class= 'interfazUsuario_container'>
    <img class="iconUsuario" src="../assets/iconUsuario.png">
    <h2 class="nombreUsuario">Dr. {{ nombre }}</h2><br/>
    <h4 class="identificacion">CC. {{ identificacion }}</h4>
  </div>
</template>

<script>
import axios from "axios";
import jwt_decode from "jwt-decode";

export default {
  name: 'InterfazUsuario',
  data: function() {
    return {
      nombre: "",
      identificacion: "",
    };
  },

   methods:{

      getData: async function () {
        
        if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
          this.$emit('logOut');
          return;
        }

        await this.verifyToken();

        let token = localStorage.getItem("token_access");
        let userId = jwt_decode(token).user_id.toString();

        axios.get(`https://meditic-be-2.herokuapp.com/user/${userId}/`,
          {
            headers: {'Authorization': `Bearer ${token}`}
          })
            .then((result) => {
              this.nombre = result.data.Nombre;
              this.identificacion = result.data['CC.'];
            })
            .catch((error) => {
              alert(error)
              this.$emit('logOut');
            });
    },

    verifyToken: function () {
      return axios.post("https://meditic-be-2.herokuapp.com/refresh/",
      {
        refresh: localStorage.getItem("token_refresh")},
        {
          headers: {}
        })
          .then((result) => {
            localStorage.setItem("token_access", result.data.access);
          })
          .catch(() => {
            this.$emit('logOut');
          });
        },
      },
      
      created: async function(){
        this.getData();
      }
}
</script>

<style>

.interfazUsuario_container{
  margin: 20px;
  
  border: black 3px solid;
  
}
.iconUsuario{
  display: inline-block;
  width: 4em;
  height: 4em;
  margin-left: 10px;
  margin-top:10px
}

.nombreUsuario{
  display: inline-block;
  position: relative;
  font-size: 1,5em;
  margin:5px;
  left:10px;
  bottom: 30px;
}
.identificacion{
  display: inline-block;
  position: relative;
  font-size: 1em;
  margin: 5px;
  left: 21%;
  bottom: 35px;
  

}
</style>
