import pdf2image

def image_conversion(inpath,image_path):
    print("Converting to image")
    OUTPUT_FOLDER= None
    FIRST_PAGE= None
    LAST_PAGE= None
    FORMAT= 'jpg'
    USERPWD= None
    USE_CROPBOX= False
    STRICT= False

    pil_images= pdf2image.convert_from_path(inpath, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, 
                                            fmt=FORMAT, userpw= USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)
    i=0
    for image in pil_images:
        i=i+1
        image.save(image_path+str(i)+'image_converted.jpg')
    
inpath= "inpath/B224-TENDER_DOC-B224-000-81-41-CP-T-8102_A_RenditionFile.pdf"
image_path= "image_path/"
image_conversion(inpath, image_path)