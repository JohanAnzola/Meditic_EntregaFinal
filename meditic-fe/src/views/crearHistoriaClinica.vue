<template>
  <div class="crearHistoriaClinica">
    <div class="crearHistoria_container">
      <h3>Historia clinica</h3>
      <form v-on:submit.prevent="crearHistoriaClinica">

        <input type="text" v-model="historia.dniPaciente" placeholder =  "DNI paciente" />
        <br />
        <input type="text" v-model="historia.motivoConsulta" placeholder = "Motivo de la consulta" />
        <br />
        <input type="text" v-model="historia.medicamentosFormulados" placeholder="Medicamentos formulados" />
        <br />
        <button type="submit">Crear Historia Clinica</button>
        
      </form>

    </div>
  </div>
</template>

<script>
import axios from "axios";
import jwt_decode from "jwt-decode";

export default {
  name: 'crear_historia',

  data: function() {
    return {
      historia: {
        motivoConsulta: "",
        medicamentosFormulados: "",
        dniPaciente: "",
        ccMedico: "",
      }
    }
  },

  methods: {
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
              this.historia.ccMedico = result.data["CC."];
            })
            .catch((error) => {
              alert(error)
              this.$emit('logOut');
            });
    },

    crearHistoriaClinica: async function(){
        if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
          this.$emit('logOut');
          return;
        }
        
        await this.verifyToken();
        console.log(this.historia);
        let token = localStorage.getItem("token_access");
        
        axios.post(`https://meditic-be-2.herokuapp.com/historias_clinicas/`,
          this.historia,
          {
            headers: {'Authorization': `Bearer ${token}`}
          })
            .then((result) => {
              alert("Se creó la historia clinica satisfactoriamente")
              this.$emit("loadHome");
            })
            .catch((error) => {
              alert(error)
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
.crearHistoriaClinica {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}

 .crearHistoria_container {
  border: 3px solid #283747;
  border-radius: 10px;
  width: 25%;
  height: 60%;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.crearHistoria_container h3 {
  color: #4e93d0;
}

.crearHistoria_container form {
  width: 70%;
}

.crearHistoria_container input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 2px solid #4e93d0;
}

.crearHistoria_container button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #186cc5;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0;
}

.crearHistoria_container button:hover {
  color: #e5e7e9;
  background: #4E93D0;
  border: 2px solid #4e93d0;
}
</style>

