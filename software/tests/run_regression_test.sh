time nosetests \
  -ds \
  --with-coverage \
  --cover-html \
  --cover-erase \
  --cover-package=dftModel,harmonicModel,hprModel,hpsModel,sineModel,sprModel,spsModel,stft,stochasticModel,utilFunctions,dftModel_function,harmonicModel_function,hprModel_function,hpsModel_function,notebook,sineModel_function,sprModel_function,spsModel_function,stft_function,stochasticModel_function,harmonicTransformations,hpsTransformations,sineTransformations,stftTransformations,stochasticTransformations,harmonicTransformations_function,hpsMorph_function,hpsTransformations_function,notebook,sineTransformations_function,stftMorph_function,stochasticTransformations_function \
  regression_test.py

## list the packages for coverage (--cover-package)
# import os, glob
# py_files = [os.path.splitext(os.path.basename(file))[0] for file in
#     glob.glob('../models*/*.py') + glob.glob('../transformations*/*.py')
#     if 'GUI' not in file
# ]
# print(','.join(py_files))
