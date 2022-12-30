import nibabel as nib
from nipype.interfaces import fsl

# Load the input image
img = nib.load("input.nii.gz")

# Create an instance of the N4BiasFieldCorrection interface
n4 = fsl.N4BiasFieldCorrection()

# Set the input image and output image filename
n4.inputs.input_image = "input.nii.gz"
n4.inputs.output_image = "output.nii.gz"

# Run the N4 bias correction
n4.run()
