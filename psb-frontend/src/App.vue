<template>
<div class='mainpage'>
<nav class="navbar navbar-expand-lg ">
  <a class="navbar-brand" href="/">
  <img src="https://i.ibb.co/NYyTVWt/PSB-logo-white-png.png" alt="PSB-logo-white-png" border="0">

  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Частным лицам <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Малому бизнесу</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Среднему бизнесу</a>
      </li>

      <li class="nav-item">
        <a class="nav-link" href="#">Корпорациям</a>
      </li>

    </ul>
  </div>
</nav>
</div>

</template>

<script>

export default {
  name: 'App',
}

</script>

<style>
nav {
   background-color: #323242 !important;
   font-size: 16px;
   line-height: 24px;
   font-weight: 400;
}

img {
   width:90px;
   height:90px;
   display:inline-block;
}

.nav-link {

   padding: 16px 0;
   display: inline-block;
   cursor: pointer;
   color: #fff;
   font-size: 13px;
   line-height: 18px;
   font-weight: 600;
   position: relative;
   font-family: 'Arial', sans-serif;
}
</style>
