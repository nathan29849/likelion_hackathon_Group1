$(function(){
    var rating = document.querySelectorAll('.rating');
    
    rating.each(function(){
        var targetScore = $(this).attr('data-rate');
        console.log(targetScore);
        $(this).find('svg:nth:-child(-n+3)'.css({color:'#F05522'}))
    });
});