# link_Preview

link_preview is now a fashionable way of sharing links in social media. 
The contents of what the preview is made up are:-

        1. og.title:-
            Title of the preview. 
            In HTML: <meta property="og.title" content="XYZ">
            Value: XYZ
            
        2. og.description:-
            Description of the preview.
            In HTML: <meta property="og.description" content="XYZ">
            Value: XYZ
            
        3. og.image:-
            Image of the preview.
            In HTML: <meta property="og.image" content="XYZ">
            Value: XYZ
            
        4. title:-
            if 'og:title' is not found, this becomes the Title.
           	In HTML: <title>XYZ</title>
            Value: XYZ
            
        5. meta description:-
            if 'og:description' is not found, this becomes the Description.
            In HTML: <meta name="description" content="XYZ">
            Value: XYZ
            
        6. favicon:-
            if 'og:image' is not found, this becomes the Image.
            In HTML: <link rel="shortcut icon" href="XYZ" type="image/x-icon">
            Value: XYZ
            
        7. website:-
            Host website for the link.
            
   Reference:- [richpreview](https://richpreview.com) (from where I learned)
    
   This module fetches all these data and combines those into a dictionary.
    
   A sample WhatsApp link_preview:-
    
        #######################################
        #   I    #    Title                   #
        #   M    #    Description             #
        #   A    #                            #
        #   G    #    website                 #
        #   E    #                            #
        #######################################
    
   Usage:-
		
        import link_preview
        dict_elem = link_preview.generate_dict(url) # this is a dict()
        
   		# Access values
        title = dict_elem['title']
        description = dict_elem['description']
        image = dict_elem['image']
        website = dict_elem['website']