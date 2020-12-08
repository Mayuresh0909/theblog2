var select=document.getElementById('Event');
function selectedvalue() {
  var optionvalue=document.querySelector("#EventCategory").value;
  switch (optionvalue) {
    case "TECHNICAL":
      while (select.options.length>0) {
        select.options.remove(0);
      }
      var arr=[];
      arr=["HACKATHON","MOCK PLACEMENT","SOFTWARE DOCUMENTATION","TECHNOHUNT",
            "BLIND CODE","CHEMSHALA",
            "TECH EXPO","PROTOTYPE",
            "TECHNICAL POSTER PRESENTATION",
            "TECHNICAL QUIZ"];
            for (var i = 0; i < arr.length; i++) {
              var option=document.createElement("option");
              var txt=document.createTextNode(arr[i]);
              option.appendChild(txt);
              option.setAttribute("value",arr[i]);
              select.insertBefore(option,select.lastChild);
            }
      break;
    case "GAMING":
      while (select.options.length>0) {
        select.options.remove(0);
      }
      var arrg=[];
      arrg=["PUBG","LIVE CS","FIFA","LAN GAMING"];
            for (var i = 0; i < arrg.length; i++) {
              var option=document.createElement("option");
              var txt=document.createTextNode(arrg[i]);
              option.appendChild(txt);
              option.setAttribute("value",arrg[i]);
              select.insertBefore(option,select.lastChild);
            }
    break;
    case "DANCE":
      while (select.options.length>0) {
        select.options.remove(0);
      }
      var arrd=[];
      arrd=["SOLO DANCE","GROUP DANCE","DUET"];
            for (var i = 0; i < arrd.length; i++) {
              var option=document.createElement("option");
              var txt=document.createTextNode(arrd[i]);
              option.appendChild(txt);
              option.setAttribute("value",arrd[i]);
              select.insertBefore(option,select.lastChild);
            }
      break;
    case "SINGING":
      while (select.options.length>0) {
        select.options.remove(0);
      }
      var arrs=[];
      arrs=["SOLO SINGING","DUET","INSTRUMENTAL","BAND WARS"];
            for (var i = 0; i < arrs.length; i++) {
              var option=document.createElement("option");
              var txt=document.createTextNode(arrs[i]);
              option.appendChild(txt);
              option.setAttribute("value",arrs[i]);
              select.insertBefore(option,select.lastChild);
            }
      break;
    case "ARTISTRY":
      while (select.options.length>0) {
        select.options.remove(0);
      }
      var arra=[];
      arra=["FILMZ","PICTURESQUE","STORY & POETRY","FACE PAINTING","TEESH ART"];
            for (var i = 0; i < arra.length; i++) {
              var option=document.createElement("option");
              var txt=document.createTextNode(arra[i]);
              option.appendChild(txt);
              option.setAttribute("value",arra[i]);
              select.insertBefore(option,select.lastChild);
            }
      break;
    case "FUN":
      while (select.options.length>0) {
        select.options.remove(0);
      }
      var arrf=[];
      arrf=["CSI(MURDER MYSTERY)",
              "ESCAPE THE ROOM",
              "ELOCUTION",
              "SCAVENGER HUNT",
              "WATER WARRIOR",
              "FASHION SHOW",
              "DEBATE",
              "WOLF OF WALL STREET",
              "SALT ACT",
              "INQUISITIVE",
              "TREASURE HUNT"];
            for (var i = 0; i < arrf.length; i++) {
              var option=document.createElement("option");
              var txt=document.createTextNode(arrf[i]);
              option.appendChild(txt);
              option.setAttribute("value",arrf[i]);
              select.insertBefore(option,select.lastChild);
            }
      break;
    case "SPORTS":
      while (select.options.length>0) {
        select.options.remove(0);
      }
      var arrsp=[];
      arrsp=["BOX CRICKET",
              "3 A-SIDE FUTSAL",
              "FIELD CRICKET",
              "CHESS",
              "FOOTBALL LEAGUE",
              "NEON CRICKET",
              "CARROM(DUET)",
              "INTERDEPARTMENT FOOTBALL",
              "ONE ON ONE CRICKET",
              "CARROM(SINGLES)",
              "ANTI CHESS",
              "BADMINTON",
              "ATHLETICS",
              "KABBADI",
              "KHO-KHO",
              "TUG OF WAR"];
            for (var i = 0; i < arrsp.length; i++) {
              var option=document.createElement("option");
              var txt=document.createTextNode(arrsp[i]);
              option.appendChild(txt);
              option.setAttribute("value",arrsp[i]);
              select.insertBefore(option,select.lastChild);
            }
      break;
    case "SIGMA":
      while (select.options.length>0) {
        select.options.remove(0);
      }
      var arrsg=[];
      arrsg=["MUDRAKALA",
              "CRESCENDO",
              "CREW 5678",
              "THE LITERATURE CLUB",
              "NAUTANKI",
              "CAMERA"];
            for (var i = 0; i < arrsg.length; i++) {
              var option=document.createElement("option");
              var txt=document.createTextNode(arrsg[i]);
              option.appendChild(txt);
              option.setAttribute("value",arrsg[i]);
              select.insertBefore(option,select.lastChild);
            }
      break;
    default:
      alert("Select proper Category");

  }
}
