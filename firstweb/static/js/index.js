let phone = document.querySelector('[href="#phone"]');
phone.onclick = e=>{
    if (confirm("即将跳转到作者页面，是否继续？")) {  
    location.href = "https://space.bilibili.com/259650532/dynamic"
} else {  
    alert("您已取消！")  
}
}

let quit = document.querySelector('[href="#quit"]');

quit.onclick = e=>{
    if (confirm("即将退出登录，是否继续？")) {  
    location.href = "/?tk=quit"
}else{
    alert("您已取消！")
}
}

let video = document.getElementById("dio")  
let numb = document.getElementsByClassName("cont")
// let p = document.querySelectorAll("p")
// p.forEach(e =>{
//     e.onclick = func =>{
//         console.log(e.innerHTML,func.target)
//     }
// }
// )
let a = document.getElementById("yes")
a.addEventListener('click',function(event){
    if (event.target.matches(".cli")){
        let vio = document.getElementById("dio")
        let deo = document.getElementById("hm")
        vio.src = vio.src.split("/").slice(0,-1).join("/") + "/"+event.target.innerHTML + ".mp4"
        console.log(vio.src)
        deo.load()
        
    }
})
   
let master = document.getElementById("hm")

document.addEventListener('keydown', function(event) {  
    var video = document.getElementById('master');  
  
    // 监听键盘事件  
      // 检查是否是空格键被按下  
      if (event.key === ' ') {  
        // 如果视频正在播放，则暂停；如果视频已暂停，则播放  
        if (video.paused) {  
          video.play();  
        } else {  
          video.pause();  
        }  
      }  
    });  
     
let dio = document.getElementById("hm")
dio.onplay = e =>{
    e.target.style.opacity = 1.0
}