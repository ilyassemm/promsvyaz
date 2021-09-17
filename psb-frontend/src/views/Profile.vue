<template>
    <div class="page-profile">
<div class='greeting'>
   <p>Здравствуйте, пользователь с id {{ APIData.ID }}!</p>
</div>

            <div class="column is-12 profile_button">
                <button @click="logout()" class="button btn btn-danger">Выйти из аккаунта</button>
            </div>

    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'

export default {
    name: 'Profile',

    data() {
        return {
        APIData: []
}
},
    mounted() {
        document.title = 'ПромСвязьБанк| Профиль пользователя'
    },

    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("id")
            this.$router.push('/')
            document.title = 'ПромСвязьБанк'
        },
	show_info() {
	         const user = localStorage.getItem('id')	
                 axios
                .get(`/analysis/${user}`)
          .then(response => {
            this.APIData = response.data
	    console.log(APIData)
          })
          .catch(err => {
            console.log(err)
          })
	},
    },


        beforeMount() {
	this.show_info()
    },
}
</script>

<style>
   .profile_button {
   padding:1rem;
}
</style>