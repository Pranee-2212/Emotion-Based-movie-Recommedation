let form=document.getElementById("formEvent");
let text=document.getElementById("text");
let submit=document.getElementById("btn");

let result=document.getElementById("result");

let createTitle=(title)=>{
     let h2=document.createElement("h2");
     h2.textContent=`Predicted Emotion is : ${title}`;
     result.appendChild(h2);
}

let createMovieCard=(movie)=>{
     let div = document.createElement("div");
     let moviePoster=document.createElement("img");
     let movieTitle=document.createElement("h2");
     let movieRelease=document.createElement("h4");
     let movieOverview=document.createElement("p");
     
     moviePoster.src=movie['poster_link'];
     moviePoster.classList.add("poster")
     movieTitle.textContent=movie['title'];
     movieTitle.classList.add("titel")
     movieRelease.textContent=movie['release_date'];
     movieRelease.classList.add("titel")
     movieOverview.textContent=movie['overview'];
     movieOverview.classList.add("titel")

     div.appendChild(moviePoster);
     div.appendChild(movieTitle);
     div.appendChild(movieOverview);
     div.appendChild(movieRelease);

     return div;

}
form.addEventListener("submit",(e)=>{
     e.preventDefault();
     let textData=text.value; 
     let url='/predict'


     fetch(url,{
          method:"POST",
          headers:{
               'Content-Type':'application/json'
          },
          body:JSON.stringify({ text:textData })
     }).then(response=>response.json())
     .then(data=>{
          createTitle(data['emotion'])
          for (let i=0;i<data['items_count'];i++){
               let div=createMovieCard(data['movies'][i])
               result.appendChild(div);
          }

    })
})
