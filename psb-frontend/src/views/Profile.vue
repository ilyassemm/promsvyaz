<template>
    <div class="page-profile">
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
        return {}
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
        }
    },
}
</script>

<style>
   .profile_button {
   padding:1rem;
}
</style>