REGISTRY = {}

from .rnn_agent import RNNAgent

from .arn_agent import ArnAgent
from .arn_rnn_agent import ArnRNNAgent
from .arn_diff_type_agent import ArnDiffAgent
from .arn_diff_type_rnn_agent import ArnDiffRnnAgent
from .arn_wo_share_diff_type_agent import ArnDiffWoShareAgent

from .dense_agent import DenseAgent
from .dense_rnn_agent import DenseRNNAgent
from .dense_rnn_dueling_agent import DenseRNNDuelingAgent
from .dense_rnn_attention_agent import DenseRNNAttentionAgent


REGISTRY["rnn"] = RNNAgent

# modify add agent type
REGISTRY["arn"] = ArnAgent
REGISTRY['arn_rnn'] = ArnRNNAgent
REGISTRY['arn_diff'] = ArnDiffAgent
REGISTRY['arn_wo_share_diff'] = ArnDiffWoShareAgent
REGISTRY['arn_diff_rnn'] = ArnDiffRnnAgent

REGISTRY['dense'] = DenseAgent
REGISTRY['dense_rnn'] = DenseRNNAgent
REGISTRY['dense_rnn_dueling'] = DenseRNNDuelingAgent
REGISTRY['dense_rnn_attention'] = DenseRNNAttentionAgent