// THIS RELOADS THE ENTIRE PAGE AS SOON AS A FORM IS SUBMITTED
function refreshPage(){
   console.log("Refreshing page");
   location.reload ? location.reload() : location = location;
}
