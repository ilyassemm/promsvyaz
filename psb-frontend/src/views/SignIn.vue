<template>
<div class='columns'>
<div class="column is-4 is-offset-4">
<form>
  <div class="form-group">
    <input type="id" class="form-control" id="id" aria-describedby="emailHelp" placeholder="Введите id пользователя">
  </div>
  <div class="form-group">
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Введите пароль">
  </div>
  <button type="submit" class="btn btn-outline-secondary">Войти</button>
</form>
</div>
</div>
</template>

<script>

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
