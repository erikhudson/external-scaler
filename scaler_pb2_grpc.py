# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import scaler_pb2 as scaler__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in scaler_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ExternalScalerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IsActive = channel.unary_unary(
                '/externalscaler.ExternalScaler/IsActive',
                request_serializer=scaler__pb2.ScaledObjectRef.SerializeToString,
                response_deserializer=scaler__pb2.IsActiveResponse.FromString,
                _registered_method=True)
        self.GetMetricSpec = channel.unary_unary(
                '/externalscaler.ExternalScaler/GetMetricSpec',
                request_serializer=scaler__pb2.ScaledObjectRef.SerializeToString,
                response_deserializer=scaler__pb2.GetMetricSpecResponse.FromString,
                _registered_method=True)
        self.GetMetrics = channel.unary_unary(
                '/externalscaler.ExternalScaler/GetMetrics',
                request_serializer=scaler__pb2.GetMetricsRequest.SerializeToString,
                response_deserializer=scaler__pb2.GetMetricsResponse.FromString,
                _registered_method=True)


class ExternalScalerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def IsActive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetricSpec(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExternalScalerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IsActive': grpc.unary_unary_rpc_method_handler(
                    servicer.IsActive,
                    request_deserializer=scaler__pb2.ScaledObjectRef.FromString,
                    response_serializer=scaler__pb2.IsActiveResponse.SerializeToString,
            ),
            'GetMetricSpec': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetricSpec,
                    request_deserializer=scaler__pb2.ScaledObjectRef.FromString,
                    response_serializer=scaler__pb2.GetMetricSpecResponse.SerializeToString,
            ),
            'GetMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetrics,
                    request_deserializer=scaler__pb2.GetMetricsRequest.FromString,
                    response_serializer=scaler__pb2.GetMetricsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'externalscaler.ExternalScaler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('externalscaler.ExternalScaler', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ExternalScaler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def IsActive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/externalscaler.ExternalScaler/IsActive',
            scaler__pb2.ScaledObjectRef.SerializeToString,
            scaler__pb2.IsActiveResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetMetricSpec(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/externalscaler.ExternalScaler/GetMetricSpec',
            scaler__pb2.ScaledObjectRef.SerializeToString,
            scaler__pb2.GetMetricSpecResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/externalscaler.ExternalScaler/GetMetrics',
            scaler__pb2.GetMetricsRequest.SerializeToString,
            scaler__pb2.GetMetricsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
