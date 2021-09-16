<template>
<div class='columns'>
<div class="column is-4 is-offset-4">
<form @submit.prevent="submitForm">
  <div class="form-group">
    <input type="id" class="form-control" id="id" v-model="username" aria-describedby="emailHelp" placeholder="Введите id пользователя">
  </div>
  <div class="form-group">
    <input type="password" class="form-control" id="exampleInputPassword1" v-model="password"  placeholder="Введите пароль">
  </div>
  <button type="submit" class="btn btn-outline-secondary">Войти</button>
</form>
</div>
</div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'
export default {
    name: 'SignIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
  methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token") 
            const formData = {
                username: this.username,
                password: this.password
            }
            await axios
                .post("/auth/login/", formData)
                .then(response => {
                    const token = response.data.key
		    console.log(response)
                    console.log(response.data.key)
                    localStorage.setItem('token', token)             
                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    const toPath = this.$route.query.to || '/profile'
                    this.$router.push(toPath)
                    
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Что-то пошло не так, попробуйте снова')
                        
                        console.log(JSON.stringify(error))
                    }
                })
        }
    },
    mounted () { 
         document.title = 'ПромСвязьБанк | Вход'
    }
} 
</script>

<style>
.columns {
   text-align:-moz-center;
   display: inline list-item;
   font-family: 'Arial', sans-serif;
}

.column {
   width:50%;
   min-width:320px;
}

form {
   margin: 0 auto;
}

</style>
