
const f = () => {
    console.log('Hello World');
    const div1 = document.createElement('div');
    div1.classList.add("container");
    const claints = ['avi','ben','david','daniel','eli','guy','gadi','haim','idan','jacob','kobi','liran','moran','nir','omer','ron','shay','tal','uri','yosi','ziv'];
    claints.forEach ( (claint) => {
        const button = document.createElement('button');
        button.innerText = `for ${claint} cleck me`;
        button.onclick = () => {
            alert(`Hello ${claint}`);
        }
        button.classList.add("my-button");
        div1.appendChild(button)
    })
    document.body.appendChild(div1);
}

f();