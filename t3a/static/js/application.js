$( document ).ready(function() {
    
  /* Show / Hide main Navigation */
    $('#nav--toggle').on('click', function(e) {
        e.preventDefault();
        $('.nav--main').toggleClass('active');
    });
    
  /* Composer Flag "Tooltips" */
    $('#flag-russia').hover(function() {
      $('#flag-info-russia').toggleClass( "active" );
    });
    $('#flag-usa').hover(function() {
      $('#flag-info-usa').toggleClass( "active" );
    });
    $('#flag-china').hover(function() {
      $('#flag-info-china').toggleClass( "active" );
    });
    
    $('#question-mars').hover(function() {
      $('#dan-everett').toggleClass( "active" );
    });
    
    
  /* Global Objects */
    var $window = $(window); /* DOM Window */
    var $anchor = $("#anchor"); /* Global "Anchor" Link for Navigation */
    
    
  /* Scroll to Next Page Section on Anchor Click */
    $anchor.on('click', function() {
        var $windowScrollTop = $window.scrollTop();
        var $windowScrollBottom = $windowScrollTop + $window.height();
        var sectionsAfter = [];

        $('section').each(function() {
            $this = $(this);
            if($this.offset().top + $this.height() > $windowScrollBottom + 85) {
                sectionsAfter.push($this[0]);
            }
        });

       $window.scrollTo(sectionsAfter[0], 1500);
    });
    
  /* Hide Anchor Arrow After 5th "slide" */  
    $window.scroll(function() {
        var $scroll = $window.scrollTop();
        var $windowHeight = $window.height();
        var $hidePoint = $windowHeight * 5;
        
        if ($scroll >= $hidePoint) {
            $anchor.addClass("hideAnchor");
        } else {
            $anchor.removeClass("hideAnchor");
        }
    });

});