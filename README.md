###  Post-Processing
the automated tool to Post-Processing the data Brain Tumor include n4 bias Correction and Skull Stripinng

* PostProcessig dataset Brast2020;

    this tool built based on top of BET algorithm that publish from [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BET) and [N4baisCorrection](https://pubmed.ncbi.nlm.nih.gov/20378467/) we automated the process and handle the data in 3D shape

    * installation Requires packages
           
        ```python
          pip install -r requirements.txt
        ```

	* tool description ;

        we develpoed a simple tool that helps to Post Processing the dstaset 
        * N4 bais Correction field this will increase the Low intensity of the image to run :</br>

        ```python
        python Postprocessing.py --config 'data_Brast.yaml' --path Processed --n4baiscorrection 
        ```

        * Skull Stripping this technic helps to reduce tissues such skull and midbrain .. only we do care about in our project is brain tissues to tun it :</br>

        ```python
        python Postprocessing.py --config 'data_Brast.yaml' --path Processed --skull_stripping 
        ```

    * Virtualization  dataset Brast2020;
     
    to vitualize few samples from the data you need to run this command 

    the Options to plot the corrected with oring img 
    type_plot{option 1 = Anat ,option 2 = epi ,option= img }

        ```python      
        python virtaulizer.py --corrected_samples --type_plot option  
        ```
    for rendering the images in 3D or 2d slices you will need to run 

            ```python
                python virtaulizer.py --v2Drender && echo 
                this will render images in 2D "
            ```
            
            ```python
            python virtualizer.py --v3Drender && echo 
             "this commaned may takes will depends on the GPU perfomence you have " 
             ```   
        

