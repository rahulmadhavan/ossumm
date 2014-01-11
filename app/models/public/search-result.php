<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>:: Ossumm ::</title>
<link href="css/theme.css" rel="stylesheet" type="text/css" />
<script src="js/jquery-1.10.2.min.js" type="text/javascript"></script>
<script src="js/jquery.lazyload.min.js" type="text/javascript"></script>
<script src="js/masonry.js" type="text/javascript"></script>
<script src="js/main.js"></script>
</head>

<body onload="mason()">


	
<form action="" method="get">

<!-- Page Container Starts Here -->
<div class="fLeft fullStretch resultContainer">
	
    <!-- Top Bar Starts Here -->
    <div class="fLeft fullStretch searchMenu">
        
        	<div class="logoUnit"><img src="images/logo-inner.png" border="0"/></div>
    	
        <!-- Search Bar Container Starts Here -->
        <div class="searchContainer">
        
        	<!-- Search Text Filed Container Starts Here -->
            <div class="fLeft search">
            <input class="fLeft" name="search" type="text" placeholder="Search Your Moodbaord" id="explorebox"/>
            <input name="Search" type="submit" class="fLeft" />
            </div>
            <!-- Search Text Filed Container Starts Here -->
            
            <!-- Quck Search Starts Here -->
            <ul class="fLeft fullStretch searchExample">
                <li>Example:</li>
                <li><a href="http://localhost/public/search-result.php?search=2013">2013</a></li>
                <li>/</li>
                <li><a href="http://localhost/public/search-result.php?search=snow">snow</a></li>
                <li>/</li>
                <li><a href="http://localhost/public/search-result.php?search=horizon">horizon</a></li>
                <li>/</li>
                <li><a href="http://localhost/public/search-result.php?search=vivid">vivid</a></li>
                <li>/</li>
                <li><a href="http://localhost/public/search-result.php?search=blaze">blaze</a></li>
            </ul>
            <!-- Quck Search Ends Here -->
            
        </div>
        <!-- Search Bar Container Ends Here -->
        
    </div>
    <!-- Top Bar Ends Here -->
    
    <!-- Search Result Container Starts Here -->
    <div class="fLeft fullStretch showResults" id="results-dev" >
    
    	<!-- Search Result Item Starts Here. Reapeat This -->
		<?
			
			require_once $_SERVER['DOCUMENT_ROOT'].'/models/aggregators/impl/SimpleImageAggregator.php';
		
			$options = array(
		  			'http'=>array(
		    			'method'=>"GET",
		    			'header'=> 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko)                        		Chrome/31.0.1650.63 Safari/537.36' 
		  				)
					);
		
			$images = SimpleImageAggregator::getInstance()->fetchImages(array("options" => $options, "searchterm" => $_GET["search"]));
		//	echo "".sizeof($images);
			$div = "<div class='fLeft resultItem'>%s</div>";
			foreach($images as $image){
			  	echo sprintf($div,$image->getHtml());
			}			
		
		?>
<!--        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div>  
      	<div class="fLeft resultItem"><img src="images/01.jpg" border="0" data-original="images/01.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/02.jpg" border="0" data-original="images/02.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/03.jpg" border="0" data-original="images/03.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/04.jpg" border="0" data-original="images/04.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/05.jpg" border="0" data-original="images/05.jpg"/></div>
        <div class="fLeft resultItem"><img src="images/06.jpg" border="0" data-original="images/06.jpg"/></div> 
-->
   	<!-- Search Result Item Ends Here -->
        
    </div>
    <!-- Search Result Container Ends Here -->
    
	<!-- Footer Container Starts Here -->    
    <div class="fLeft fullStretch footerContainer">
    Hi
    </div>
	<!-- Footer Container Ends Here -->
    
</div>
<!-- Page Container Ends Here -->

</form>

</body>
</html>
