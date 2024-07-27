let img = document.querySelector('img')
skip = document.querySelector("[href='#']")
function base64(){
    fetch("/mkimg")
    .then((response) => response.json())
    .then((data)=> {
        img.src = data.img
    })
    .catch(error=>{console.log("error")})}
base64()
skip.onclick = e=>{
    base64()
}
// document.getElementById('dl').addEventListener('submit', function(event) {  
//     let value = document.getElementById('mima').value;  
//     let regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;  
//     let errorDiv = document.getElementById('error');  
  
//     if (!regex.test(value)) {  
//         errorDiv.textContent = '密码必须包含大写字母、小写字母、数字和特殊字符，且长度至少为8。';  
//         event.preventDefault(); // 阻止表单提交  
//     } else {  
//         errorDiv.innerText = ""; // 清除错误消息  
//         // 如果需要，可以在这里继续表单的提交逻辑，但在这个例子中我们不需要  
//     }    
// });  