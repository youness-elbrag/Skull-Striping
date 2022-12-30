###  Post-Processing
the automated tool to Post-Processing the data Brain Tumor include n4 bias Correction and Skull Stripinng

* PostProcessig dataset Brast2020;

    this tool built based on top of BET algorithm that publish from [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BET) and [N4baisCorrection](https://pubmed.ncbi.nlm.nih.gov/20378467/) we automated the process and handle the data in 3D shape

	* tool description ;

        we develpoed a simple tool that helps to Post Processing the dstaset 
        * N4 bais Correction field this will increase the Low intensity of the image to run :

        ```python
        python Postprocessing.py --config 'data_Brast.yaml' --path path_name  --n4baiscorrection 
        ```

        * Skull Stripping this technic helps to reduce tissues such skull and midbrain .. only we do care about in our project is brain tissues to tun it :

        ```python
        python Postprocessing.py --config 'data_Brast.yaml' --path path_name --skull_stripping 
        ```

