# Keras h5py truncated file error debugging

This is a simple repository designed to reproduce the error found in [this
issue](https://github.com/keras-team/keras/issues/6221). I assume you've got
Keras set up before you try this.

The error in question occurs when you try to create a VGG16 model in keras,
e.g. `model = VGG16(weights='imagenet')`, and looks something like:
```
IOError: Unable to open file (Truncated file: eof = 21463040, sblock->base_addr = 0, stored_eoa = 58889256)
```

When you create a model in Keras, it will check the `~/.keras/models` directory
to see if the model's data file exists, otherwise it will download it. However,
if a download was somehow interrupted, the data file may exist under
`~/.keras/models` but be incomplete. This is what results in the above error.
The solution is to delete the broken data file and rerun the Python code
creating the model, ensuring that you wait for the download to complete
successfully.

An intentionally truncated data file,
`vgg16_weights_tf_dim_ordering_tf_kernels_truncated.h5` is included in this
repo to simulate an interrupted download. To recreate the error, first run
`./copy_truncated_model.sh` to copy the truncated model into your
`~/.keras/models` directory. Then try running `./debug.py`, which tries to load
the model and run an image through it; you should see the error. `debug.py` is
a bare bones script adapted from the [Keras docs](https://github.com/keras-team/keras).

To fix it, just delete
`~./keras/models/vgg16_weights_tf_dim_ordering_tf_kernels.h5` and rerun
`./debug.py`, waiting for the download to complete. The prediction on the cat
image should now work.

I included the broken data file with the repo because its a little bit of a
pain to create one. If you run `./debug.py` and ctrl-c while its downloaded the
model, the program is smart enough to remove the incomplete file from
`~/.keras/models` so the error does not occur. I created the included truncated
data file by backgrounding the process and then killing it with the `kill`
command.
