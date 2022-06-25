from email.mime import image

cdn = 'https://cdn.ethereal.bond/file/github-images/'
imageTags = []
imageData = []
altText = []

def findImageData(markdownfile):
    with open(markdownfile,'r+') as infile:
        lines = infile.readlines()
    
    for line in lines:
        if line.startswith('![['):
            imageTags.append(line.rstrip())
      
    for line in imageTags:
        
        imageData.append(line.split(' ')[2].split(']')[0])
    
    infile.close()
    return imageData,imageTags

def formatConverter(oldimagenames): #take the images and extensions and provide it as a list
    imagesFormatted = []
    for imagename in oldimagenames:
        formattedimagename = f'![]({cdn}Pasted+image+{imagename})'
        imagesFormatted.append(formattedimagename)
    return imagesFormatted

def fileFormatWriter(filename):
    with open(filename, 'r+') as infile:
        lines = infile.readlines() #read file as entire string
        
        i = 0
        j= 0
        newFileContents = [] #create list that will contain contents of newly formatted file
        for line in lines:
            j = j+1
            if line.startswith('![['):
                newFileContents.append(line.replace(line, convertedData[i]+'\n')) #if line fits that ![[ syntax, append.
                i = i+1
            else:
                newFileContents.append(line) #append everything else that doesn't meet the above syntax.
        print(lines)
                
    
        infile.seek(0)
        infile.writelines(newFileContents)
        infile.close()

if __name__=='__main__':
    markdownfile = input('Enter the markdown file you would like to convert to Github\'s image formatting ')
    imageData, imageTags = findImageData(markdownfile)
    convertedData = formatConverter(imageData) #the updated image tags put through the formatconverter function.
    fileFormatWriter(markdownfile)

#![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)  .... Example Github Image Formatting
