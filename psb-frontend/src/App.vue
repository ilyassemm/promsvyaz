<template>
<div class='mainpage'>
<!--Header-->
<header>
  <nav class="navbar navbar-expand-lg sm-2">
   <a class="navbar-brand" href="/">
    <img src="@/assets/PSB_logo_white_png.png" alt="PSB-logo-white-png" >
   </a>
   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon">≡</span>
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

      <li class="nav-item signin">
        <a class="nav-link signin" href="/signin">Вход</a>
      </li>

     </ul>
   </div>
  </nav>
</header>
<!--Header-->

</div>
  <router-view/>

<!--Footer-->
<footer class=" text-center text-lg-start">
  <div class="text-center p-3">
    2021 © Прототип разработан командой Cogwheel для ПСБ:
    <a class = 'nav-link github' href="https://github.com/ilyassemm/promsvyaz.git">Github</a>
  </div>
</footer>
<!--Footer-->
</template>

<script>
/* eslint-disable */
</script>


<style>
.navbar-toggler {
   background-color: transparent !important;
}

.navbar-toggler-icon {
  color: aliceblue;
  font-size: 300%;
}
header {
   width:100%;
}
nav {
   background-color: #323242 !important;
   font-size: 16px;
   line-height: 24px;
   font-weight: 400;
}
img {
   width:141px;
   height:100px;
   display:inline-block;
}
.nav-link {
   padding: 16px 0;
   text-decoration:none;
   cursor: pointer;
   color: white !important;
   font-size: 13px;
   line-height: 18px;
   font-weight: 600;
   position: relative;
   font-family: 'Arial', sans-serif;
}
.nav-link {
text-decoration:none; /*Убираем стандартное подчёркивание ссылки если оно ещё не убрано*/
display: inline-block; /*делаем чтобы наша ссылка из строчного элемента превратилась в строчно-блочный */
line-height: 1; /*Задаём высоту строки (можно в пикселях)*/
color:#2F73B6;/*Задаём цвет ссылки*/
}
.nav-link:after {
display: block; /*превращаем его в блочный элемент*/
content: ""; /*контента в данном блоке не будет поэтому в кавычках ничего не ставим*/
height: 3px; /*задаём высоту линии*/
width: 0%; /*задаём начальную ширину элемента (линии)*/
background-color: white; /*цвет фона элемента*/
transition: width 0.4s ease-in-out; /*данное свойство отвечает за плавное изменение ширины. Здесь можно задать время анимации в секундах (в данном случае задано 0.4 секунды)*/
}
.nav-link:hover:after,
.nav-link:focus:after {
   width: 100%;
}
.nav-link:hover{
color:white;
}

footer {
   background-color: #323242 !important;
   color:white;
}


</style>
