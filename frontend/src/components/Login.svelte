<script>
    let Rol;
    let Email;
    let Contrasena;

    function handleClick() {

        console.log(Rol,Email,Contrasena);
    }

</script>


<style>
    body{
        background-color: #F4E9DF;
    }
    #login {
        margin-top: 6rem;
        width: 30%;
    }
    #input {
        margin-top: 1rem;
        border-radius: 0.3rem;
    }
    .Boton{
        width: 100%;
        border-radius: 2rem;
    }

</style>


<body>

<div class="text-center">

    <p>Gestionin</p>
</div>

<div class="container " id="login">
    <p >Soy un...</p>

    <form class="form">
        <div class="btn-group mb-4  Boton" role="group" aria-label="Basic radio toggle button group">
            <input type="radio" class="btn-check" name="btnradio" id="btnradio1"  value="Putaso" >
            <label class="btn btn-outline-dark" for="btnradio1">Putaso</label>
            <input type="radio" class="btn-check" name="btnradio" id="btnradio2"  value="Trolaso"  checked>
            <label class="btn btn-outline-dark" for="btnradio2">Trolaso</label>
        </div>
        <div class="form-group">
            <input type="email" class="form-control text-center"  aria-describedby="emailHelp" placeholder="Enter email" bind:value = {(Email)} >
            <input type="password" class="form-control text-center " id="input" placeholder="Contraseña" bind:value = {(Contrasena)} >
        </div>
    </form>
    <button type="submit" class="btn btn-dark btn-lg text-center mt-4 Boton" on:click={handleClick} >Siguiente</button>

</div>
</body>