window.onload = function(){
     var mylink = document.getElementsByClassName('my-link')[0],
     paragraph = document.getElementById('paragraph');
	 mylink.onclick = function() {
         if (paragraph.style.visibility == '') {
             paragraph.style.visibility = 'hidden';
         } 
		 else {
             paragraph.style.visibility = '';
          };
        return false;
    };
};