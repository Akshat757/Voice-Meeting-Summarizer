from deepmultilingualpunctuation import PunctuationModel

def punctuator(text):
    model = PunctuationModel()
    result = model.restore_punctuation(text)
    print(result)
    return result

# text = '''in 2018 cornell researchers built a high-powered detector that in combination with an algorithm-driven process called ptychography set a world record
# by tripling the resolution of a state-of-the-art electron microscope as successful as it was that approach had a weakness it only worked with ultrathin samples that were
# a few atoms thick anything thicker would cause the electrons to scatter in ways that could not be disentangled now a team again led by david muller the samuel b eckert
# professor of engineering has bested its own record by a factor of two with an electron microscope pixel array detector empad that incorporates even more sophisticated
# 3d reconstruction algorithms the resolution is so fine-tuned the only blurring that remains is the thermal jiggling of the atoms themselves'''
# punctuator(text)

# In 2018, Cornell researchers built a high-powered detector that, in combination with an algorithm-driven process called Ptychography, set a world record by tripling the
# # resolution of a state-of-the-art electron microscope. As successful as it was, that approach had a weakness. It only worked with ultrathin samples that were a few atoms
# # thick. Anything thicker would cause the electrons to scatter in ways that could not be disentangled. Now, a team again led by David Muller, the Samuel B. 
# # Eckert Professor of Engineering, has bested its own record by a factor of two with an Electron microscope pixel array detector empad that incorporates even more
# # sophisticated 3d reconstruction algorithms. The resolution is so fine-tuned the only blurring that remains is the thermal jiggling of the atoms themselves.