<template>
  <div class="historiaClinica_container">
    <h2 class="historiaClinica_titulo">Historias Clinicas</h2>
    <label class="label_idPaciente" for="idPaciente">DNI Paciente: </label>

    <input
      type="text"
      name="idPaciente"
      class="inputPaciente"
      v-model="informacion.dni"
    /><br />

    <button
      type="submit"
      class="boton_VerHistoria"
      v-on:click="buscarHistoriasClinicas"
    >
      Ver historias
    </button>

    <div class = "historiasClinicas">
        <div class = "historiaClinica" v-for="(historia, index) in historiasClinicas" :key="index">
           <pre>
           <strong>ID Historia Clinica: {{historia['ID']}}</strong>
           <strong>DATOS DEL PACIENTE</strong>
        
           DNI: {{historia.Paciente.DNI}}         Paciente: {{historia.Paciente.Nombres}} {{historia.Paciente.Apellidos}}      Edad: {{historia.Paciente.Edad}}

           Entidad: {{historia.Paciente.Entidad}}         Correo: {{historia.Paciente.Correo}}         
           <br>
           <strong>ANTECEDENTES</strong>

           Enfermedades: {{historia.Paciente.Enfermedades}}         Alergias: {{historia.Paciente.Alergias}}
           <br>
           <strong>CONSULTA</strong>

           Motivo de la consulta: {{historia['Motivo de consulta']}}
           
           Fecha de atención: {{historia['Fecha de atencion']}}
           <br>
           <strong>DIAGNÓSTICO</strong>

           Medicamentos formulados: {{historia['Medicamentos formulados']}}
           <br>
           <strong>Dr. {{historia.Medico['Nombre completo']}}</strong>
           <strong>CC. {{historia.Medico['CC.']}}</strong>
           <strong>{{historia.Medico.Correo}}</strong>

           <button class="buttoneliminar" v-on:click="eliminarHistoriaClinica(historia['ID'])">Borrar</button>
           </pre>
            
        </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import jwt_decode from "jwt-decode";

export default {
  name: 'HistoriaClinica',

  data: function() {
    return {
      informacion: {
        dni : ""
      },

      historiasClinicas: []

    };
  },

  methods: {
    buscarHistoriasClinicas: async function(){
      console.log("buscando");
      if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
          this.$emit('logOut');
          return;
        }

        await this.verifyToken();

        let token = localStorage.getItem("token_access");

        axios.post("https://meditic-be-2.herokuapp.com/historias_clinicas/paciente/",
         this.informacion,
          {
            headers: {'Authorization': `Bearer ${token}`},
          },
          )
            .then((result) => {
               this.historiasClinicas = [];
               this.historiasClinicas.length = 0;
              
               
               this.historiasClinicas = result.data;
               for(let i = 0; i < this.historiasClinicas.length ; i++){
                    let localDate = new Date(this.historiasClinicas[i]['Fecha de atencion']);
                    this.historiasClinicas[i]['Fecha de atencion'] = localDate.toLocaleString();
               }
               console.log(this.historiasClinicas);
            })
            .catch((error) => {
              this.$emit('logOut');
          });

    },
      eliminarHistoriaClinica: async function(historiaid){

      if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
          this.$emit('logOut');
          return;
        }

        await this.verifyToken();

        let token = localStorage.getItem("token_access");
        let url = 'https://meditic-be-2.herokuapp.com/historia_clinica/'+historiaid
        let config = {
            headers: {'Authorization': `Bearer ${token}`},
          }
        axios.delete(url,
         this.informacion,
          {
            headers: {'Authorization': `Bearer ${token}`},
          },
          ).then(function(){
            console.log("ingreso al then");
            
          })
          .catch((error) => {
              this.$emit('logOut');
          })
        this.buscarHistoriasClinicas()
          

    },
    CrearHistoriaClinica: function(){
      
      localStorage.setItem("dni", this.dni);
      this.$emit('loadCrearHistoria');
      alert("hola")
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

  }

}
</script>

<style>
.historiaClinica_container {
  margin-top: 20px;
  margin-right: 20px;
  width: 63%;
  height: auto;
  border: black 3px solid;
  float: right;
}
.historiaClinica_titulo {
  font-size: 4em;
  text-align: center;
  color: #4e93d0;
}
.label_idPaciente {
  margin-left: 20px;
  font-size: 21px;
  margin-left: 21%;
}
.inputPaciente {
  margin: 1px 10px;
  width: 21em;
  height: 2em;
  font-size: 14px;
  border: 2px solid #4e93d0;
  border-radius: 9999px;
}

.boton_VerHistoria {
  margin: 20px;
  background: #4e93d0;
  color: aliceblue;
  width: 8em;
  height: 2em;
  margin-left: 21%;
  font-size: 1em;
}


.historiasClinicas {
  margin: 150px auto;
  width: 600px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.historiaClinica {
  border: solid 2px black;
  font-size: 14px;
}
.buttoneliminar{
    
    background: #4e93d0;
    color: aliceblue;
    margin-left: 30%;
    font-size: 1em;
}
</style>


