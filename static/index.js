const date= new Date().getFullYear()

const footer=document.querySelector('.footer');

footer.innerHTML=`
    <p> &copy; ${date} Flask series
`