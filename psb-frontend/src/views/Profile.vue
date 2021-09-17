<template>
<div class="page-profile">

<div class='greeting'>
   <p>Здравствуйте, пользователь с id {{ APIData.ID }}! У нас для тебя немного рекомендаций!</p>
</div>

<div v-for="links in Result" :key="links" class="col-sm-2 recomendations">
<div class="btn-group">
<button type="button" class="btn btn-outline-secondary recommendations__button">{{links}}</button>
</div>
</div>

<div v-for="links in Result" :key="links" class="col-sm-2 recomendations">
<div class="btn-group">
{{links}} <br>
</div>
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
        APIData: [],
	Result: []
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
	    	   console.log(this.APIData)
	   	   if (this.APIData.Major == true) {
			console.log('да')
	   		this.Result.push('https://www.psbank.ru/Personal/DebetCards/YourPSB_premium?tab=2')
	  		}
	   if (this.APIData.Traveller == true) {
	   this.Result.push('https://www.psbank.ru/Personal/DebetCards/WorldDebet')
	  }

	   if (this.APIData.Hamster == true) {
	   this.Result.push('https://www.psbank.ru/Personal/DebetCards/YourCashback')
	  }

	   if (this.APIData.Wide == true) {
	   this.Result.push('https://www.psbank.ru/Personal/DebetCards/YourCashback')
	  }

	   if (this.APIData.Poor == true) {
	   this.Result.push('https://www.psbank.ru/Personal/CreditCards/100_Plus')
	  }

	   if (this.APIData.Burn == true) {
	   this.Result.push('https://www.psbank.ru/Personal/CreditCards/DoubleCashback')
	  }

	   if (this.APIData.Migrant == true) {
	   this.Result.push('https://www.psbank.ru/Personal/DebetCards/YourBank')
	  }

	   if (this.APIData.Fitmost == true) {
	   this.Result.push('https://www.fitmost.ru/')
	  }

	   if (this.APIData.Flowers == true) {
	   this.Result.push('https://www.turandot-palace.ru/')
	  }

	   if (this.APIData.Coffee == true) {
	   this.Result.push('https://tastycoffee.ru/')
	  }


          	})

                .catch(err => {
                   /* console.log(err) */
          	})
	},

    },


    beforeMount() {
	this.show_info()
    }
}
</script>

<style>
   .profile_button {
   padding:1rem;
}

.recommendations__button {
  width:30rem;
}

.recomendations {
  text-align:center;
}
</style>