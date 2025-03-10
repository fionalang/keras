"""Commonly-used neural network operations not included in NumPy."""

from keras import backend
from keras.api_export import keras_export
from keras.backend import KerasTensor
from keras.backend import any_symbolic_tensors
from keras.backend import standardize_data_format
from keras.backend.common.backend_utils import (
    compute_conv_transpose_output_shape,
)
from keras.ops import operation_utils
from keras.ops.operation import Operation
from keras.ops.operation_utils import reduce_shape


class Relu(Operation):
    def call(self, x):
        return backend.nn.relu(x)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(["keras.ops.relu", "keras.ops.nn.relu"])
def relu(x):
    """Rectified linear unit activation function.

    It is defined as `f(x) = max(0, x)`.

    Args:
        x: Input tensor.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x1 = keras.ops.convert_to_tensor([-1.0, 0.0, 1.0, 0.2])
    >>> keras.ops.relu(x1)
    array([0.0, 0.0, 1.0, 0.2], dtype=float32)
    """
    if any_symbolic_tensors((x,)):
        return Relu().symbolic_call(x)
    return backend.nn.relu(x)


class Relu6(Operation):
    def call(self, x):
        return backend.nn.relu6(x)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(["keras.ops.relu6", "keras.ops.nn.relu6"])
def relu6(x):
    """Rectified linear unit activation function with upper bound of 6.

    It is defined as `f(x) = np.clip(x, 0, 6)`.

    Args:
        x: Input tensor.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = keras.ops.convert_to_tensor([-3.0, -2.0, 0.1, 0.2, 6.0, 8.0])
    >>> keras.ops.relu6(x)
    array([0.0, 0.0, 0.1, 0.2, 6.0, 6.0], dtype=float32)
    """
    if any_symbolic_tensors((x,)):
        return Relu6().symbolic_call(x)
    return backend.nn.relu6(x)


class Sigmoid(Operation):
    def call(self, x):
        return backend.nn.sigmoid(x)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(["keras.ops.sigmoid", "keras.ops.nn.sigmoid"])
def sigmoid(x):
    """Sigmoid activation function.

    It is defined as `f(x) = 1 / (1 + exp(-x))`.

    Args:
        x: Input tensor.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = keras.ops.convert_to_tensor([-6.0, 1.0, 0.0, 1.0, 6.0])
    >>> keras.ops.sigmoid(x)
    array([0.00247262, 0.7310586, 0.5, 0.7310586, 0.9975274], dtype=float32)

    """
    if any_symbolic_tensors((x,)):
        return Sigmoid().symbolic_call(x)
    return backend.nn.sigmoid(x)


class Softplus(Operation):
    def call(self, x):
        return backend.nn.softplus(x)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(["keras.ops.softplus", "keras.ops.nn.softplus"])
def softplus(x):
    """Softplus activation function.

    It is defined as `f(x) = log(exp(x) + 1)`, where `log` is the natural
    logarithm and `exp` is the exponential function.

    Args:
        x: Input tensor.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = keras.ops.convert_to_tensor([-0.555, 0.0, 0.555])
    >>> keras.ops.softplus(x)
    array([0.45366603, 0.6931472, 1.008666], dtype=float32)

    """
    if any_symbolic_tensors((x,)):
        return Softplus().symbolic_call(x)
    return backend.nn.softplus(x)


class Softsign(Operation):
    def call(self, x):
        return backend.nn.softsign(x)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(["keras.ops.softsign", "keras.ops.nn.softsign"])
def softsign(x):
    """Softsign activation function.

    It is defined as `f(x) = x / (abs(x) + 1)`.

    Args:
        x: Input tensor.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = keras.ops.convert_to_tensor([-0.100, -10.0, 1.0, 0.0, 100.0])
    >>> keras.ops.softsign(x)
    Array([-0.09090909, -0.90909094, 0.5, 0.0, 0.990099], dtype=float32)

    """
    if any_symbolic_tensors((x,)):
        return Softsign().symbolic_call(x)
    return backend.nn.softsign(x)


class Silu(Operation):
    def call(self, x):
        return backend.nn.silu(x)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(
    [
        "keras.ops.silu",
        "keras.ops.nn.silu",
        "keras.ops.swish",
        "keras.ops.nn.swish",
    ]
)
def silu(x):
    """Sigmoid Linear Unit (SiLU) activation function, also known as Swish.

    The SiLU activation function is computed by the sigmoid function multiplied
    by its input. It is defined as `f(x) = x * sigmoid(x)`.

    Args:
        x: Input tensor.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = keras.ops.convert_to_tensor([-6.0, 1.0, 0.0, 1.0, 6.0])
    >>> keras.ops.sigmoid(x)
    array([0.00247262, 0.7310586, 0.5, 0.7310586, 0.9975274], dtype=float32)
    >>> keras.ops.silu(x)
    array([-0.0148357, 0.7310586, 0.0, 0.7310586, 5.9851646], dtype=float32)

    """
    if any_symbolic_tensors((x,)):
        return Silu().symbolic_call(x)
    return backend.nn.silu(x)


class LogSigmoid(Operation):
    def call(self, x):
        return backend.nn.log_sigmoid(x)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(
    [
        "keras.ops.log_sigmoid",
        "keras.ops.nn.log_sigmoid",
    ]
)
def log_sigmoid(x):
    """Logarithm of the sigmoid activation function.

    It is defined as `f(x) = log(1 / (1 + exp(-x)))`.

    Args:
        x: Input tensor.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = keras.ops.convert_to_tensor([-0.541391, 0.0, 0.50, 5.0])
    >>> keras.ops.log_sigmoid(x)
    array([-1.0000418, -0.6931472, -0.474077, -0.00671535], dtype=float32)

    """
    if any_symbolic_tensors((x,)):
        return LogSigmoid().symbolic_call(x)
    return backend.nn.log_sigmoid(x)


class LeakyRelu(Operation):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.negative_slope = negative_slope

    def call(self, x):
        return backend.nn.leaky_relu(x, self.negative_slope)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(["keras.ops.leaky_relu", "keras.ops.nn.leaky_relu"])
def leaky_relu(x, negative_slope=0.2):
    """Leaky version of a Rectified Linear Unit activation function.

    It allows a small gradient when the unit is not active, it is defined as:

    `f(x) = alpha * x for x < 0` or `f(x) = x for x >= 0`.

    Args:
        x: Input tensor.
        negative_slope: Slope of the activation function at x < 0.
            Defaults to `0.2`.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = np.array([-1., 0., 1.])
    >>> x_leaky_relu = keras.ops.leaky_relu(x)
    >>> print(x_leaky_relu)
    array([-0.2,  0. ,  1. ], shape=(3,), dtype=float64)

    """
    if any_symbolic_tensors((x,)):
        return LeakyRelu(negative_slope).symbolic_call(x)
    return backend.nn.leaky_relu(x, negative_slope=negative_slope)


class HardSigmoid(Operation):
    def call(self, x):
        return backend.nn.hard_sigmoid(x)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(
    [
        "keras.ops.hard_sigmoid",
        "keras.ops.nn.hard_sigmoid",
    ]
)
def hard_sigmoid(x):
    """Hard sigmoid activation function.

    It is defined as:

    `0 if x < -2.5`, `1 if x > 2.5`, `(0.2 * x) + 0.5 if -2.5 <= x <= 2.5`.

    Args:
        x: Input tensor.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = np.array([-1., 0., 1.])
    >>> x_hard_sigmoid = keras.ops.hard_sigmoid(x)
    >>> print(x_hard_sigmoid)
    array([0.3, 0.5, 0.7], shape=(3,), dtype=float64)

    """
    if any_symbolic_tensors((x,)):
        return HardSigmoid().symbolic_call(x)
    return backend.nn.hard_sigmoid(x)


class HardSilu(Operation):
    def call(self, x):
        return backend.nn.hard_silu(x)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(
    [
        "keras.ops.hard_silu",
        "keras.ops.nn.hard_silu",
        "keras.ops.hard_swish",
        "keras.ops.nn.hard_swish",
    ]
)
def hard_silu(x):
    """Hard SiLU activation function, also known as Hard Swish.

    It is defined as:

    - `0` if `if x < -3`
    - `x` if `x > 3`
    - `x * (x + 3) / 6` if `-3 <= x <= 3`

    It's a faster, piecewise linear approximation of the silu activation.

    Args:
        x: Input tensor.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = keras.ops.convert_to_tensor([-3.0, -1.0, 0.0, 1.0, 3.0])
    >>> keras.ops.hard_silu(x)
    array([-0.0, -0.3333333, 0.0, 0.6666667, 3.0], shape=(5,), dtype=float32)

    """
    if any_symbolic_tensors((x,)):
        return HardSilu().symbolic_call(x)
    return backend.nn.hard_silu(x)


class Elu(Operation):
    def __init__(self, alpha=1.0):
        super().__init__()
        self.alpha = alpha

    def call(self, x):
        return backend.nn.elu(x, alpha=self.alpha)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(["keras.ops.elu", "keras.ops.nn.elu"])
def elu(x, alpha=1.0):
    """Exponential Linear Unit activation function.

    It is defined as:

    `f(x) =  alpha * (exp(x) - 1.) for x < 0`, `f(x) = x for x >= 0`.

    Args:
        x: Input tensor.
        alpha: A scalar, slope of positive section. Defaults to `1.0`.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = np.array([-1., 0., 1.])
    >>> x_elu = keras.ops.elu(x)
    >>> print(x_elu)
    array([-0.63212055, 0., 1.], shape=(3,), dtype=float64)

    """
    if any_symbolic_tensors((x,)):
        return Elu(alpha).symbolic_call(x)
    return backend.nn.elu(x, alpha=alpha)


class Selu(Operation):
    def call(self, x):
        return backend.nn.selu(x)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(["keras.ops.selu", "keras.ops.nn.selu"])
def selu(x):
    """Scaled Exponential Linear Unit (SELU) activation function.

    It is defined as:

    `f(x) =  scale * alpha * (exp(x) - 1.) for x < 0`,
    `f(x) = scale * x for x >= 0`.

    Args:
        x: Input tensor.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = np.array([-1., 0., 1.])
    >>> x_selu = keras.ops.selu(x)
    >>> print(x_selu)
    array([-1.11133055, 0., 1.05070098], shape=(3,), dtype=float64)

    """
    if any_symbolic_tensors((x,)):
        return Selu().symbolic_call(x)
    return backend.nn.selu(x)


class Gelu(Operation):
    def __init__(self, approximate=True):
        super().__init__()
        self.approximate = approximate

    def call(self, x):
        return backend.nn.gelu(x, self.approximate)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(["keras.ops.gelu", "keras.ops.nn.gelu"])
def gelu(x, approximate=True):
    """Gaussian Error Linear Unit (GELU) activation function.

    If `approximate` is `True`, it is defined as:
    `f(x) = 0.5 * x * (1 + tanh(sqrt(2 / pi) * (x + 0.044715 * x^3)))`

    Or if `approximate` is `False`, it is defined as:
    `f(x) = x * P(X <= x) = 0.5 * x * (1 + erf(x / sqrt(2)))`,
    where `P(X) ~ N(0, 1)`.

    Args:
        x: Input tensor.
        approximate: Approximate version of GELU activation. Defaults to `True`.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = np.array([-1., 0., 1.])
    >>> x_gelu = keras.ops.gelu(x)
    >>> print(x_gelu)
    array([-0.15865525, 0., 0.84134475], shape=(3,), dtype=float64)

    """
    if any_symbolic_tensors((x,)):
        return Gelu(approximate).symbolic_call(x)
    return backend.nn.gelu(x, approximate)


class Softmax(Operation):
    def __init__(self, axis=-1):
        super().__init__()
        self.axis = axis

    def call(self, x):
        return backend.nn.softmax(x, axis=self.axis)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(["keras.ops.softmax", "keras.ops.nn.softmax"])
def softmax(x, axis=-1):
    """Softmax activation function.

    The elements of the output vector lie within the range `(0, 1)`, and their
    total sum is exactly 1 (excluding the floating point rounding error).

    Each vector is processed independently. The `axis` argument specifies the
    axis along which the function is applied within the input.

    It is defined as:
    `f(x) = exp(x) / sum(exp(x))`

    Args:
        x: Input tensor.
        axis: Integer, axis along which the softmax is applied.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = np.array([-1., 0., 1.])
    >>> x_softmax = keras.ops.softmax(x)
    >>> print(x_softmax)
    array([0.09003057, 0.24472847, 0.66524096], shape=(3,), dtype=float64)

    """
    if any_symbolic_tensors((x,)):
        return Softmax(axis).symbolic_call(x)
    if isinstance(axis, tuple):
        original_shape = x.shape
        new_shape = []
        skip_dims = set(axis)
        i = 0
        while i < len(original_shape):
            if i in skip_dims:
                size = 1
                while i in skip_dims:
                    size *= original_shape[i]
                    i += 1
                new_shape.append(size)
            else:
                new_shape.append(original_shape[i])
                i += 1
        x = backend.numpy.reshape(x, new_shape)
        x = backend.nn.softmax(x, axis=-1)
        x = backend.numpy.reshape(x, original_shape)
        return x
    else:
        return backend.nn.softmax(x, axis=axis)


class LogSoftmax(Operation):
    def __init__(self, axis=-1):
        super().__init__()
        self.axis = axis

    def call(self, x):
        return backend.nn.log_softmax(x, axis=self.axis)

    def compute_output_spec(self, x):
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(
    [
        "keras.ops.log_softmax",
        "keras.ops.nn.log_softmax",
    ]
)
def log_softmax(x, axis=-1):
    """Log-softmax activation function.

    It is defined as:
    `f(x) = x - max(x) - log(sum(exp(x - max(x))))`

    Args:
        x: Input tensor.
        axis: Integer, axis along which the log-softmax is applied.
            Defaults to `-1`.

    Returns:
        A tensor with the same shape as `x`.

    Example:

    >>> x = np.array([-1., 0., 1.])
    >>> x_log_softmax = keras.ops.log_softmax(x)
    >>> print(x_log_softmax)
    array([-2.40760596, -1.40760596, -0.40760596], shape=(3,), dtype=float64)

    """
    if any_symbolic_tensors((x,)):
        return LogSoftmax(axis).symbolic_call(x)
    if isinstance(axis, tuple):
        original_shape = x.shape
        new_shape = []
        skip_dims = set(axis)
        i = 0
        while i < len(original_shape):
            if i in skip_dims:
                size = 1
                while i in skip_dims:
                    size *= original_shape[i]
                    i += 1
                new_shape.append(size)
            else:
                new_shape.append(original_shape[i])
                i += 1
        x = backend.numpy.reshape(x, new_shape)
        x = backend.nn.log_softmax(x, axis=-1)
        x = backend.numpy.reshape(x, original_shape)
        return x
    else:
        return backend.nn.log_softmax(x, axis=axis)


class MaxPool(Operation):
    def __init__(
        self,
        pool_size,
        strides=None,
        padding="valid",
        data_format=None,
    ):
        super().__init__()
        self.pool_size = pool_size
        self.strides = strides
        self.padding = padding.lower()
        self.data_format = data_format

    def call(self, inputs):
        return backend.nn.max_pool(
            inputs,
            self.pool_size,
            self.strides,
            self.padding,
            self.data_format,
        )

    def compute_output_spec(self, inputs):
        output_shape = operation_utils.compute_pooling_output_shape(
            inputs.shape,
            self.pool_size,
            self.strides,
            self.padding,
            self.data_format,
        )
        return KerasTensor(output_shape, dtype=inputs.dtype)


@keras_export(["keras.ops.max_pool", "keras.ops.nn.max_pool"])
def max_pool(
    inputs,
    pool_size,
    strides=None,
    padding="valid",
    data_format=None,
):
    """Max pooling operation.

    Args:
        inputs: Tensor of rank N+2. `inputs` has shape
            `(batch_size,) + inputs_spatial_shape + (num_channels,)` if
            `data_format="channels_last"`, or
            `(batch_size, num_channels) + inputs_spatial_shape` if
            `data_format="channels_first"`. Pooling happens over the spatial
            dimensions only.
        pool_size: int or tuple/list of integers of size
            `len(inputs_spatial_shape)`, specifying the size of the pooling
            window for each spatial dimension of the input tensor. If
            `pool_size` is int, then every spatial dimension shares the same
            `pool_size`.
        strides: int or tuple/list of integers of size
            `len(inputs_spatial_shape)`. The stride of the sliding window for
            each spatial dimension of the input tensor. If `strides` is int,
            then every spatial dimension shares the same `strides`.
        padding: string, either `"valid"` or `"same"`. `"valid"` means no
            padding is applied, and `"same"` results in padding evenly to the
            left/right or up/down of the input such that output has the
            same height/width dimension as the input when `strides=1`.
        data_format: A string, either `"channels_last"` or `"channels_first"`.
            `data_format` determines the ordering of the dimensions in the
            inputs. If `data_format="channels_last"`, `inputs` is of shape
            `(batch_size, ..., channels)` while if
            `data_format="channels_first"`, `inputs` is of shape
            `(batch_size, channels, ...)`.

    Returns:
        A tensor of rank N+2, the result of the max pooling operation.
    """
    data_format = standardize_data_format(data_format)
    padding = padding.lower()
    if any_symbolic_tensors((inputs,)):
        return MaxPool(
            pool_size,
            strides,
            padding,
            data_format,
        ).symbolic_call(inputs)
    return backend.nn.max_pool(inputs, pool_size, strides, padding, data_format)


class AveragePool(Operation):
    def __init__(
        self,
        pool_size,
        strides=None,
        padding="valid",
        data_format=None,
    ):
        super().__init__()
        self.pool_size = pool_size
        self.strides = strides
        self.padding = padding.lower()
        self.data_format = data_format

    def call(self, inputs):
        return backend.nn.average_pool(
            inputs,
            self.pool_size,
            self.strides,
            self.padding,
            self.data_format,
        )

    def compute_output_spec(self, inputs):
        output_shape = operation_utils.compute_pooling_output_shape(
            inputs.shape,
            self.pool_size,
            self.strides,
            self.padding,
            self.data_format,
        )
        return KerasTensor(output_shape, dtype=inputs.dtype)


@keras_export(
    [
        "keras.ops.average_pool",
        "keras.ops.nn.average_pool",
    ]
)
def average_pool(
    inputs,
    pool_size,
    strides=None,
    padding="valid",
    data_format=None,
):
    """Average pooling operation.

    Args:
        inputs: Tensor of rank N+2. `inputs` has shape
            `(batch_size,) + inputs_spatial_shape + (num_channels,)` if
            `data_format="channels_last"`, or
            `(batch_size, num_channels) + inputs_spatial_shape` if
            `data_format="channels_first"`. Pooling happens over the spatial
            dimensions only.
        pool_size: int or tuple/list of integers of size
            `len(inputs_spatial_shape)`, specifying the size of the pooling
            window for each spatial dimension of the input tensor. If
            `pool_size` is int, then every spatial dimension shares the same
            `pool_size`.
        strides: int or tuple/list of integers of size
            `len(inputs_spatial_shape)`. The stride of the sliding window for
            each spatial dimension of the input tensor. If `strides` is int,
            then every spatial dimension shares the same `strides`.
        padding: string, either `"valid"` or `"same"`. `"valid"` means no
            padding is applied, and `"same"` results in padding evenly to the
            left/right or up/down of the input such that output has the
            same height/width dimension as the input when `strides=1`.
        data_format: A string, either `"channels_last"` or `"channels_first"`.
            `data_format` determines the ordering of the dimensions in the
            inputs. If `data_format="channels_last"`, `inputs` is of shape
            `(batch_size, ..., channels)` while if
            `data_format="channels_first"`, `inputs` is of shape
            `(batch_size, channels, ...)`.

    Returns:
        A tensor of rank N+2, the result of the average pooling operation.
    """
    data_format = standardize_data_format(data_format)
    padding = padding.lower()
    if any_symbolic_tensors((inputs,)):
        return AveragePool(
            pool_size,
            strides,
            padding,
            data_format,
        ).symbolic_call(inputs)
    return backend.nn.average_pool(
        inputs, pool_size, strides, padding, data_format
    )


class Conv(Operation):
    def __init__(
        self,
        strides=1,
        padding="valid",
        data_format=None,
        dilation_rate=1,
    ):
        super().__init__()
        self.strides = strides
        self.padding = padding.lower()
        self.data_format = data_format
        self.dilation_rate = dilation_rate

    def call(self, inputs, kernel):
        return backend.nn.conv(
            inputs,
            kernel,
            strides=self.strides,
            padding=self.padding,
            data_format=self.data_format,
            dilation_rate=self.dilation_rate,
        )

    def compute_output_spec(self, inputs, kernel):
        output_shape = operation_utils.compute_conv_output_shape(
            inputs.shape,
            kernel.shape[-1],
            kernel.shape[:-2],
            self.strides,
            self.padding,
            self.data_format,
            self.dilation_rate,
        )
        return KerasTensor(output_shape, dtype=inputs.dtype)


@keras_export(["keras.ops.conv", "keras.ops.nn.conv"])
def conv(
    inputs,
    kernel,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
):
    """General N-D convolution.

    This ops supports 1D, 2D and 3D convolution.

    Args:
        inputs: Tensor of rank N+2. `inputs` has shape
            `(batch_size,) + inputs_spatial_shape + (num_channels,)` if
            `data_format="channels_last"`, or
            `(batch_size, num_channels) + inputs_spatial_shape` if
            `data_format="channels_first"`.
        kernel: Tensor of rank N+2. `kernel` has shape
            `(kernel_spatial_shape, num_input_channels, num_output_channels)`.
            `num_input_channels` should match the number of channels in
            `inputs`.
        strides: int or int tuple/list of `len(inputs_spatial_shape)`,
            specifying the strides of the convolution along each spatial
            dimension. If `strides` is int, then every spatial dimension shares
            the same `strides`.
        padding: string, either `"valid"` or `"same"`. `"valid"` means no
            padding is applied, and `"same"` results in padding evenly to the
            left/right or up/down of the input such that output has the
            same height/width dimension as the input when `strides=1`.
        data_format: A string, either `"channels_last"` or `"channels_first"`.
            `data_format` determines the ordering of the dimensions in the
            inputs. If `data_format="channels_last"`, `inputs` is of shape
            `(batch_size, ..., channels)` while if
            `data_format="channels_first"`, `inputs` is of shape
            `(batch_size, channels, ...)`.
        dilation_rate: int or int tuple/list of `len(inputs_spatial_shape)`,
            specifying the dilation rate to use for dilated convolution. If
            `dilation_rate` is int, then every spatial dimension shares
            the same `dilation_rate`.

    Returns:
        A tensor of rank N+2, the result of the conv operation.
    """
    data_format = standardize_data_format(data_format)
    padding = padding.lower()
    if any_symbolic_tensors((inputs,)):
        return Conv(strides, padding, data_format, dilation_rate).symbolic_call(
            inputs, kernel
        )
    return backend.nn.conv(
        inputs, kernel, strides, padding, data_format, dilation_rate
    )


class DepthwiseConv(Operation):
    def __init__(
        self,
        strides=1,
        padding="valid",
        data_format=None,
        dilation_rate=1,
    ):
        super().__init__()
        self.strides = strides
        self.padding = padding.lower()
        self.data_format = data_format
        self.dilation_rate = dilation_rate

    def call(self, inputs, kernel):
        return backend.nn.depthwise_conv(
            inputs,
            kernel,
            self.strides,
            self.padding,
            self.data_format,
            self.dilation_rate,
        )

    def compute_output_spec(self, inputs, kernel):
        output_shape = operation_utils.compute_conv_output_shape(
            inputs.shape,
            kernel.shape[-1] * kernel.shape[-2],
            kernel.shape[:-2],
            self.strides,
            self.padding,
            self.data_format,
            self.dilation_rate,
        )
        return KerasTensor(output_shape, dtype=inputs.dtype)


@keras_export(
    [
        "keras.ops.depthwise_conv",
        "keras.ops.nn.depthwise_conv",
    ]
)
def depthwise_conv(
    inputs,
    kernel,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
):
    """General N-D depthwise convolution.

    This ops supports 1D and 2D depthwise convolution.

    Args:
        inputs: Tensor of rank N+2. `inputs` has shape
            `(batch_size,) + inputs_spatial_shape + (num_channels,)` if
            `data_format="channels_last"`, or
            `(batch_size, num_channels) + inputs_spatial_shape` if
            `data_format="channels_first"`.
        kernel: Tensor of rank N+2. `kernel` has shape
            [kernel_spatial_shape, num_input_channels, num_channels_multiplier],
            `num_input_channels` should match the number of channels in
            `inputs`.
        strides: int or int tuple/list of `len(inputs_spatial_shape)`,
            specifying the strides of the convolution along each spatial
            dimension. If `strides` is int, then every spatial dimension shares
            the same `strides`.
        padding: string, either `"valid"` or `"same"`. `"valid"` means no
            padding is applied, and `"same"` results in padding evenly to the
            left/right or up/down of the input such that output has the
            same height/width dimension as the input when `strides=1`.
        data_format: A string, either `"channels_last"` or `"channels_first"`.
            `data_format` determines the ordering of the dimensions in the
            inputs. If `data_format="channels_last"`, `inputs` is of shape
            `(batch_size, ..., channels)` while if
            `data_format="channels_first"`, `inputs` is of shape
            `(batch_size, channels, ...)`.
        dilation_rate: int or int tuple/list of `len(inputs_spatial_shape)`,
            specifying the dilation rate to use for dilated convolution. If
            `dilation_rate` is int, then every spatial dimension shares
            the same `dilation_rate`.

    Returns:
        A tensor of rank N+2, the result of the depthwise conv operation.
    """
    data_format = standardize_data_format(data_format)
    padding = padding.lower()
    if any_symbolic_tensors((inputs,)):
        return DepthwiseConv(
            strides, padding, data_format, dilation_rate
        ).symbolic_call(inputs, kernel)
    return backend.nn.depthwise_conv(
        inputs,
        kernel,
        strides,
        padding,
        data_format,
        dilation_rate,
    )


class SeparableConv(Operation):
    def __init__(
        self,
        strides=1,
        padding="valid",
        data_format=None,
        dilation_rate=1,
    ):
        super().__init__()
        self.strides = strides
        self.padding = padding.lower()
        self.data_format = data_format
        self.dilation_rate = dilation_rate

    def call(self, inputs, depthwise_kernel, pointwise_kernel):
        return backend.nn.separable_conv(
            inputs,
            depthwise_kernel,
            pointwise_kernel,
            self.strides,
            self.padding,
            self.data_format,
            self.dilation_rate,
        )

    def compute_output_spec(self, inputs, depthwise_kernel, pointwise_kernel):
        output_shape = list(
            depthwise_conv(
                inputs,
                depthwise_kernel,
                self.strides,
                self.padding,
                self.data_format,
                self.dilation_rate,
            ).shape
        )
        if self.data_format == "channels_last":
            output_shape[-1] = pointwise_kernel.shape[-1]
        else:
            output_shape[1] = pointwise_kernel.shape[-1]
        return KerasTensor(output_shape, dtype=inputs.dtype)


@keras_export(
    [
        "keras.ops.separable_conv",
        "keras.ops.nn.separable_conv",
    ]
)
def separable_conv(
    inputs,
    depthwise_kernel,
    pointwise_kernel,
    strides=1,
    padding="valid",
    data_format=None,
    dilation_rate=1,
):
    """General N-D separable convolution.

    This ops supports 1D and 2D separable convolution. `separable_conv` is
    a depthwise conv followed by a pointwise conv.

    Args:
        inputs: Tensor of rank N+2. `inputs` has shape
            `(batch_size,) + inputs_spatial_shape + (num_channels,)` if
            `data_format="channels_last"`, or
            `(batch_size, num_channels) + inputs_spatial_shape` if
            `data_format="channels_first"`.
        depthwise_kernel: Tensor of rank N+2. `depthwise_kernel` has shape
            [kernel_spatial_shape, num_input_channels, num_channels_multiplier],
            `num_input_channels` should match the number of channels in
            `inputs`.
        pointwise_kernel: Tensor of rank N+2. `pointwise_kernel` has shape
            `(*ones_like(kernel_spatial_shape),
            num_input_channels * num_channels_multiplier, num_output_channels)`.
        strides: int or int tuple/list of `len(inputs_spatial_shape)`,
            specifying the strides of the convolution along each spatial
            dimension. If `strides` is int, then every spatial dimension shares
            the same `strides`.
        padding: string, either `"valid"` or `"same"`. `"valid"` means no
            padding is applied, and `"same"` results in padding evenly to the
            left/right or up/down of the input such that output has the
            same height/width dimension as the input when `strides=1`.
        data_format: A string, either `"channels_last"` or `"channels_first"`.
            `data_format` determines the ordering of the dimensions in the
            inputs. If `data_format="channels_last"`, `inputs` is of shape
            `(batch_size, ..., channels)` while if
            `data_format="channels_first"`, `inputs` is of shape
            `(batch_size, channels, ...)`.
        dilation_rate: int or int tuple/list of `len(inputs_spatial_shape)`,
            specifying the dilation rate to use for dilated convolution. If
            `dilation_rate` is int, then every spatial dimension shares
            the same `dilation_rate`.

    Returns:
        A tensor of rank N+2, the result of the depthwise conv operation.
    """
    data_format = standardize_data_format(data_format)
    padding = padding.lower()
    if any_symbolic_tensors((inputs,)):
        return SeparableConv(
            strides,
            padding,
            data_format,
            dilation_rate,
        ).symbolic_call(inputs, depthwise_kernel, pointwise_kernel)
    return backend.nn.separable_conv(
        inputs,
        depthwise_kernel,
        pointwise_kernel,
        strides,
        padding,
        data_format,
        dilation_rate,
    )


class ConvTranspose(Operation):
    def __init__(
        self,
        strides,
        padding="valid",
        output_padding=None,
        data_format=None,
        dilation_rate=1,
    ):
        super().__init__()
        self.strides = strides
        self.output_padding = output_padding
        self.padding = padding.lower()
        self.data_format = data_format
        self.dilation_rate = dilation_rate

    def call(
        self,
        inputs,
        kernel,
    ):
        return backend.nn.conv_transpose(
            inputs,
            kernel,
            self.strides,
            self.output_padding,
            self.padding,
            self.data_format,
            self.dilation_rate,
        )

    def compute_output_spec(self, inputs, kernel):
        kernel_size = kernel.shape[:-2]
        filters = kernel.shape[-2]
        output_shape = compute_conv_transpose_output_shape(
            inputs.shape,
            kernel_size,
            filters,
            self.strides,
            self.padding,
            self.output_padding,
            self.data_format,
            self.dilation_rate,
        )
        return KerasTensor(output_shape, dtype=inputs.dtype)


@keras_export(
    [
        "keras.ops.conv_transpose",
        "keras.ops.nn.conv_transpose",
    ]
)
def conv_transpose(
    inputs,
    kernel,
    strides,
    padding="valid",
    output_padding=None,
    data_format=None,
    dilation_rate=1,
):
    """General N-D convolution transpose.

    Also known as de-convolution. This ops supports 1D, 2D and 3D convolution.

    Args:
        inputs: Tensor of rank N+2. `inputs` has shape
            `(batch_size,) + inputs_spatial_shape + (num_channels,)` if
            `data_format="channels_last"`, or
            `(batch_size, num_channels) + inputs_spatial_shape` if
            `data_format="channels_first"`.
        kernel: Tensor of rank N+2. `kernel` has shape
            [kernel_spatial_shape, num_output_channels, num_input_channels],
            `num_input_channels` should match the number of channels in
            `inputs`.
        strides: int or int tuple/list of `len(inputs_spatial_shape)`,
            specifying the strides of the convolution along each spatial
            dimension. If `strides` is int, then every spatial dimension shares
            the same `strides`.
        padding: string, either `"valid"` or `"same"`. `"valid"` means no
            padding is applied, and `"same"` results in padding evenly to the
            left/right or up/down of the input such that output has the
            same height/width dimension as the input when `strides=1`.
        output_padding: int or int tuple/list of `len(inputs_spatial_shape)`,
            specifying the amount of padding along the height and width of
            the output tensor. Can be a single integer to specify the same
            value for all spatial dimensions. The amount of output padding
            along a given dimension must be lower than the stride along that
            same dimension. If set to `None` (default), the output shape is
            inferred.
        data_format: A string, either `"channels_last"` or `"channels_first"`.
            `data_format` determines the ordering of the dimensions in the
            inputs. If `data_format="channels_last"`, `inputs` is of shape
            `(batch_size, ..., channels)` while if
            `data_format="channels_first"`, `inputs` is of shape
            `(batch_size, channels, ...)`.
        dilation_rate: int or int tuple/list of `len(inputs_spatial_shape)`,
            specifying the dilation rate to use for dilated convolution. If
            `dilation_rate` is int, then every spatial dimension shares
            the same `dilation_rate`.

    Returns:
        A tensor of rank N+2, the result of the conv operation.
    """
    data_format = standardize_data_format(data_format)
    padding = padding.lower()
    if any_symbolic_tensors((inputs,)):
        return ConvTranspose(
            strides, padding, output_padding, data_format, dilation_rate
        ).symbolic_call(inputs, kernel)
    return backend.nn.conv_transpose(
        inputs,
        kernel,
        strides,
        padding,
        output_padding,
        data_format,
        dilation_rate,
    )


class OneHot(Operation):
    def __init__(self, num_classes, axis=-1, dtype=None):
        super().__init__()
        self.num_classes = num_classes
        self.axis = axis
        self.dtype = dtype or backend.floatx()

    def call(self, x):
        return backend.nn.one_hot(
            x, self.num_classes, axis=self.axis, dtype=self.dtype
        )

    def compute_output_spec(self, x):
        x_shape = list(getattr(x, "shape", []))
        if self.axis == -1:
            x_shape.append(self.num_classes)
        elif self.axis >= 0 and self.axis < len(x_shape):
            x_shape.insert(self.axis, self.num_classes)
        else:
            raise ValueError(
                f"axis must be -1 or between [0, {len(x.shape)}), but "
                f"received {self.axis}."
            )
        return KerasTensor(x_shape, dtype=self.dtype)


@keras_export(["keras.ops.one_hot", "keras.ops.nn.one_hot"])
def one_hot(x, num_classes, axis=-1, dtype=None):
    """Converts integer tensor `x` into a one-hot tensor.

    The one-hot encoding is a representation where each integer value is
    converted into a binary vector with a length equal to `num_classes`,
    and the index corresponding to the integer value is marked as 1, while
    all other indices are marked as 0.

    Args:
        x: Integer tensor to be encoded. The shape can be
            arbitrary, but the dtype should be integer.
        num_classes: Number of classes for the one-hot encoding.
        axis: Axis along which the encoding is performed. Defaults to
            `-1`, which represents the last axis.
        dtype: (Optional) Data type of the output tensor. If not
            provided, it defaults to the default data type of the backend.

    Returns:
        Integer tensor: One-hot encoded tensor with the same shape as `x`
        except for the specified `axis` dimension, which will have
        a length of `num_classes`. The dtype of the output tensor
        is determined by `dtype` or the default data type of the backend.

    Example:

    >>> x = keras.ops.convert_to_tensor([1, 3, 2, 0])
    >>> one_hot(x, num_classes=4)
    array([[0. 1. 0. 0.]
           [0. 0. 0. 1.]
           [0. 0. 1. 0.]
           [1. 0. 0. 0.]], shape=(4, 4), dtype=float32)
    """
    if any_symbolic_tensors((x,)):
        return OneHot(num_classes, axis=axis, dtype=dtype).symbolic_call(x)
    return backend.nn.one_hot(
        x, num_classes, axis=axis, dtype=dtype or backend.floatx()
    )


class BinaryCrossentropy(Operation):
    def __init__(self, from_logits=False):
        super().__init__()
        self.from_logits = from_logits

    def call(self, target, output):
        return backend.nn.binary_crossentropy(
            target, output, from_logits=self.from_logits
        )

    def compute_output_spec(self, target, output):
        if target.shape != output.shape:
            raise ValueError(
                "Arguments `target` and `output` must have the same shape. "
                "Received: "
                f"target.shape={target.shape}, output.shape={output.shape}"
            )
        return KerasTensor(output.shape, dtype=output.dtype)


@keras_export(
    [
        "keras.ops.binary_crossentropy",
        "keras.ops.nn.binary_crossentropy",
    ]
)
def binary_crossentropy(target, output, from_logits=False):
    """Computes binary cross-entropy loss between target and output tensor.

    The binary cross-entropy loss is commonly used in binary
    classification tasks where each input sample belongs to one
    of the two classes. It measures the dissimilarity between the
    target and output probabilities or logits.

    Args:
        target: The target tensor representing the true binary labels.
            Its shape should match the shape of the `output` tensor.
        output: The output tensor representing the predicted probabilities
            or logits. Its shape should match the shape of the
            `target` tensor.
        from_logits: (optional) Whether `output` is a tensor of logits or
            probabilities.
            Set it to `True` if `output` represents logits; otherwise,
            set it to `False` if `output` represents probabilities.
            Defaults to`False`.

    Returns:
        Integer tensor: The computed binary cross-entropy loss between
        `target` and `output`.

    Example:

    >>> target = keras.ops.convert_to_tensor([0, 1, 1, 0])
    >>> output = keras.ops.convert_to_tensor([0.1, 0.9, 0.8, 0.2])
    >>> binary_crossentropy(target, output)
    array([0.10536054 0.10536054 0.22314355 0.22314355],
          shape=(4,), dtype=float32)
    """
    if any_symbolic_tensors((target, output)):
        return BinaryCrossentropy(from_logits=from_logits).symbolic_call(
            target, output
        )
    return backend.nn.binary_crossentropy(
        target, output, from_logits=from_logits
    )


class CategoricalCrossentropy(Operation):
    def __init__(self, from_logits=False, axis=-1):
        super().__init__()
        self.from_logits = from_logits
        self.axis = axis

    def call(self, target, output):
        return backend.nn.categorical_crossentropy(
            target, output, from_logits=self.from_logits, axis=self.axis
        )

    def compute_output_spec(self, target, output):
        if target.shape != output.shape:
            raise ValueError(
                "Arguments `target` and `output` must have the same shape. "
                "Received: "
                f"target.shape={target.shape}, output.shape={output.shape}"
            )
        if len(target.shape) < 1:
            raise ValueError(
                "Arguments `target` and `output` must be at least rank 1. "
                "Received: "
                f"target.shape={target.shape}, output.shape={output.shape}"
            )
        return KerasTensor(output.shape[:-1], dtype=output.dtype)


@keras_export(
    [
        "keras.ops.categorical_crossentropy",
        "keras.ops.nn.categorical_crossentropy",
    ]
)
def categorical_crossentropy(target, output, from_logits=False, axis=-1):
    """Computes categorical cross-entropy loss between target and output tensor.

    The categorical cross-entropy loss is commonly used in multi-class
    classification tasks where each input sample can belong to one of
    multiple classes. It measures the dissimilarity
    between the target and output probabilities or logits.

    Args:
        target: The target tensor representing the true categorical labels.
            Its shape should match the shape of the `output` tensor
            except for the last dimension.
        output: The output tensor representing the predicted probabilities
            or logits. Its shape should match the shape of the `target`
            tensor except for the last dimension.
        from_logits: (optional) Whether `output` is a tensor of logits or
            probabilities.
            Set it to `True` if `output` represents logits; otherwise,
            set it to `False` if `output` represents probabilities.
            Defaults to`False`.
        axis: (optional) The axis along which the categorical cross-entropy
            is computed.
            Defaults to `-1`, which corresponds to the last dimension of
            the tensors.

    Returns:
        Integer tensor: The computed categorical cross-entropy loss between
        `target` and `output`.

    Example:

    >>> target = keras.ops.convert_to_tensor(
    ... [[1, 0, 0],
    ...  [0, 1, 0],
    ...  [0, 0, 1]])
    >>> output = keras.ops.convert_to_tensor(
    ... [[0.9, 0.05, 0.05],
    ...  [0.1, 0.8, 0.1],
    ...  [0.2, 0.3, 0.5]])
    >>> categorical_crossentropy(target, output)
    array([0.10536054 0.22314355 0.6931472 ], shape=(3,), dtype=float32)
    """
    if any_symbolic_tensors((target, output)):
        return CategoricalCrossentropy(
            from_logits=from_logits, axis=axis
        ).symbolic_call(target, output)
    return backend.nn.categorical_crossentropy(
        target, output, from_logits=from_logits, axis=axis
    )


class SparseCategoricalCrossentropy(Operation):
    def __init__(self, from_logits=False, axis=-1):
        super().__init__()
        self.from_logits = from_logits
        self.axis = axis

    def call(self, target, output):
        return backend.nn.sparse_categorical_crossentropy(
            target, output, from_logits=self.from_logits, axis=self.axis
        )

    def compute_output_spec(self, target, output):
        if len(output.shape) < 1:
            raise ValueError(
                "Argument `output` must be at least rank 1. "
                "Received: "
                f"output.shape={output.shape}"
            )
        target_shape = target.shape
        if len(target_shape) == len(output.shape) and target_shape[-1] == 1:
            target_shape = target_shape[:-1]
        if target_shape != output.shape[:-1]:
            raise ValueError(
                "Arguments `target` and `output` must have the same shape "
                "up until the last dimension: "
                f"target.shape={target.shape}, output.shape={output.shape}"
            )
        return KerasTensor(output.shape[:-1], dtype=output.dtype)


@keras_export(
    [
        "keras.ops.sparse_categorical_crossentropy",
        "keras.ops.nn.sparse_categorical_crossentropy",
    ]
)
def sparse_categorical_crossentropy(target, output, from_logits=False, axis=-1):
    """Computes sparse categorical cross-entropy loss.

    The sparse categorical cross-entropy loss is similar to categorical
    cross-entropy, but it is used when the target tensor contains integer
    class labels instead of one-hot encoded vectors. It measures the
    dissimilarity between the target and output probabilities or logits.

    Args:
        target: The target tensor representing the true class labels as
            integers. Its shape should match the shape of the `output`
            tensor except for the last dimension.
        output: The output tensor representing the predicted probabilities
            or logits.
            Its shape should match the shape of the `target` tensor except
            for the last dimension.
        from_logits: (optional) Whether `output` is a tensor of logits
            or probabilities.
            Set it to `True` if `output` represents logits; otherwise,
            set it to `False` if `output` represents probabilities.
            Defaults to`False`.
        axis: (optional) The axis along which the sparse categorical
            cross-entropy is computed.
            Defaults to `-1`, which corresponds to the last dimension
            of the tensors.

    Returns:
        Integer tensor: The computed sparse categorical cross-entropy
        loss between `target` and `output`.

    Example:

    >>> target = keras.ops.convert_to_tensor([0, 1, 2], dtype=int32)
    >>> output = keras.ops.convert_to_tensor(
    ... [[0.9, 0.05, 0.05],
    ...  [0.1, 0.8, 0.1],
    ...  [0.2, 0.3, 0.5]])
    >>> sparse_categorical_crossentropy(target, output)
    array([0.10536056 0.22314355 0.6931472 ], shape=(3,), dtype=float32)
    """
    if any_symbolic_tensors((target, output)):
        return SparseCategoricalCrossentropy(
            from_logits=from_logits, axis=axis
        ).symbolic_call(target, output)
    return backend.nn.sparse_categorical_crossentropy(
        target, output, from_logits=from_logits, axis=axis
    )


class MultiHot(Operation):
    def __init__(
        self, num_classes=None, axis=-1, dtype=None, name=None, **kwargs
    ):
        if num_classes is None and "num_tokens" in kwargs:
            num_classes = kwargs.pop("num_tokens")
        if num_classes is None:
            raise ValueError("Argument `num_classes` must be specified.")
        super().__init__(name, **kwargs)
        self.num_classes = num_classes
        self.axis = axis
        self.dtype = dtype or backend.floatx()

    def call(self, inputs):
        return backend.nn.multi_hot(
            inputs,
            num_classes=self.num_classes,
            axis=self.axis,
            dtype=self.dtype,
        )

    def compute_output_spec(self, inputs):
        x_shape = list(getattr(inputs, "shape", []))
        if self.axis == -1:
            x_shape.append(self.num_classes)
        elif self.axis >= 0 and self.axis < len(x_shape):
            x_shape.insert(self.axis, self.num_classes)
        else:
            raise ValueError(
                f"axis must be -1 or between [0, {len(inputs.shape)}), but "
                f"received {self.axis}."
            )

        if len(x_shape) == 2:
            x_shape = [x_shape[-1]]
        else:
            x_shape = [x_shape[0]] + x_shape[2:]

        return KerasTensor(x_shape, dtype=inputs.dtype)


@keras_export(
    [
        "keras.ops.multi_hot",
        "keras.ops.nn.multi_hot",
    ]
)
def multi_hot(inputs, num_classes=None, axis=-1, dtype=None, **kwargs):
    """Encodes integer labels as multi-hot vectors.

    This function encodes integer labels as multi-hot vectors, where each label
    is mapped to a binary value in the resulting vector.

    Args:
        inputs: Tensor of integer labels to be converted to multi-hot vectors.
        num_classes: Integer, the total number of unique classes.
        axis: (optional) Axis along which the multi-hot encoding should be
            added. Defaults to `-1`, which corresponds to the last dimension.
        dtype: (optional) The data type of the resulting tensor. Default
            is backend's float type.

    Returns:
        Tensor: The multi-hot encoded tensor.

    Example:

    >>> data = keras.ops.convert_to_tensor([0, 4])
    >>> keras.ops.multi_hot(data, num_classes=5)
    array([1.0, 0.0, 0.0, 0.0, 1.0], dtype=float32)

    """
    if num_classes is None and "num_tokens" in kwargs:
        num_classes = kwargs.pop("num_tokens")
    if num_classes is None:
        raise ValueError("Argument `num_classes` must be specified.")

    if any_symbolic_tensors((inputs,)):
        return MultiHot(num_classes, axis, dtype).symbolic_call(inputs)

    return backend.nn.multi_hot(inputs, num_classes, axis, dtype)


class Moments(Operation):
    def __init__(self, axes, keepdims=False, synchronized=False, name=None):
        super().__init__(name)
        self.axes = axes
        self.keepdims = keepdims
        self.synchronized = synchronized

    def call(self, x):
        return backend.nn.moments(
            x,
            axes=self.axes,
            keepdims=self.keepdims,
            synchronized=self.synchronized,
        )

    def compute_output_spec(self, x):
        return (
            KerasTensor(
                reduce_shape(x.shape, axis=self.axes, keepdims=self.keepdims),
                dtype=x.dtype,
            ),
            KerasTensor(
                reduce_shape(x.shape, axis=self.axes, keepdims=self.keepdims),
                dtype=x.dtype,
            ),
        )


@keras_export(
    [
        "keras.ops.moments",
        "keras.ops.nn.moments",
    ]
)
def moments(x, axes, keepdims=False, synchronized=False):
    """Calculates the mean and variance of `x`.

    The mean and variance are calculated by aggregating the contents of `x`
    across `axes`. If `x` is 1-D and `axes = [0]` this is just the mean and
    variance of a vector.

    Args:
        x: Input tensor.
        axes: A list of axes which to compute mean and variance.
        keepdims: If this is set to `True`, the axes which are reduced are left
            in the result as dimensions with size one.
        synchronized: Only applicable with the TensorFlow backend.
            If `True`, synchronizes the global batch statistics (mean and
            variance) across all devices at each training step in a
            distributed training strategy. If `False`, each replica uses its own
            local batch statistics.

    Returns:
        A tuple containing two tensors - mean and variance.

    Example:

    >>> x = keras.ops.convert_to_tensor([0, 1, 2, 3, 100], dtype="float32")
    >>> keras.ops.moments(x, axes=[0])
    (array(21.2, dtype=float32), array(1553.3601, dtype=float32))

    """
    if any_symbolic_tensors((x,)):
        return Moments(axes, keepdims, synchronized=synchronized).symbolic_call(
            x
        )

    return backend.nn.moments(x, axes, keepdims, synchronized=synchronized)


class BatchNorm(Operation):
    def __init__(self, axis, epsilon, name=None):
        super().__init__(name)
        self.axis = axis
        self.epsilon = epsilon

    def _check_shape(self, name, shape, expected_shape):
        if shape != expected_shape:
            raise ValueError(
                f"Arguments `{name}` must be a vector of length "
                f"`x.shape[axis]`. Expected: `{expected_shape}`. "
                f"Received: `{shape}."
            )

    def compute_output_spec(self, x, mean, variance, offset, scale):
        shape = (x.shape[self.axis],)
        self._check_shape("mean", tuple(mean.shape), shape)
        self._check_shape("variance", tuple(variance.shape), shape)
        if offset is not None:
            self._check_shape("offset", tuple(offset.shape), shape)
        if offset is not scale:
            self._check_shape("scale", tuple(scale.shape), shape)
        return KerasTensor(x.shape, dtype=x.dtype)


@keras_export(
    [
        "keras.ops.batch_normalization",
        "keras.ops.nn.batch_normalization",
    ]
)
def batch_normalization(
    x, mean, variance, axis, offset=None, scale=None, epsilon=1e-3
):
    """Normalizes `x` by `mean` and `variance`.

    This op is typically used by the batch normalization step in a neural
    network. It normalizes the input tensor along the given axis.

    Args:
        x: Input tensor.
        mean: A mean vector of the same length as the `axis` dimension of the
            input thensor.
        variance: A variance vector of the same length as the `axis` dimension
            of the input tensor.
        axis: Integer, the axis that should be normalized.
        offset: An offset vector of the same length as the `axis` dimension of
            the input tensor. If not `None`, `offset` is added to the normalized
            tensor. Defaults to `None`.
        scale: A scale vector of the same length as the `axis` dimension of the
            input tensor. If not `None`, the normalized tensor is multiplied by
            `scale`. Defaults to `None`.
        epsilon: Small float added to variance to avoid dividing by zero.
            Defaults to 1e-3.

    Returns:
        The normalized tensor.

    Example:

    >>> x = keras.ops.convert_to_tensor(
    ...     [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
    ... )
    >>> keras.ops.batch_normalization(
    ...     x,
    ...     mean=[0.4, 0.5, 0.6],
    ...     variance=[0.67, 0.67, 0.67],
    ...     axis=-1
    ... )
    array([[-3.6624e-01, -3.6624e-01, -3.6624e-01],
           [-4.6445e-09,  0.0000e+00, -1.8578e-08],
           [ 3.6624e-01,  3.6624e-01,  3.6624e-01]])

    """
    if any_symbolic_tensors((x, mean, variance, offset, scale)):
        return BatchNorm(axis, epsilon).symbolic_call(
            x, mean, variance, offset, scale
        )

    return backend.nn.batch_normalization(
        x, mean, variance, axis, offset, scale, epsilon
    )
