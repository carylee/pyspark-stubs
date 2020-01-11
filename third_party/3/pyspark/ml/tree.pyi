from typing import Any, List, Optional, Sequence
from pyspark.ml._typing import P, T

from pyspark.ml.linalg import Vector
from pyspark.ml.param.shared import *
from pyspark.ml.util import *
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel as JavaModel, JavaParams as JavaParams, JavaPredictionModel as JavaPredictionModel, JavaPredictor as JavaPredictor

class _DecisionTreeModel(JavaPredictionModel[T]):
    @property
    def numNodes(self) -> int: ...
    @property
    def depth(self) -> int: ...
    @property
    def toDebugString(self) -> str: ...
    def predictLeaf(self, value: Vector) -> float: ...

class _DecisionTreeParams(HasCheckpointInterval, HasSeed, HasWeightCol):
    leafCol: Param[str]
    maxDepth: Param[int]
    maxBins: Param[int]
    minInstancesPerNode: Param[int]
    minWeightFractionPerNode: Param[float]
    minInfoGain: Param[float]
    maxMemoryInMB: Param[int]
    cacheNodeIds: Param[bool]
    def __init__(self) -> None: ...
    def setLeafCol(self: P, value: str) -> P: ...
    def getLeafCol(self) -> str: ...
    def getMaxDepth(self) -> int: ...
    def getMaxBins(self) -> int: ...
    def getMinInstancesPerNode(self) -> int: ...
    def getMinInfoGain(self) -> float: ...
    def getMaxMemoryInMB(self) -> int: ...
    def getCacheNodeIds(self) -> bool: ...

class _TreeEnsembleModel(JavaPredictionModel[T]):
    @property
    def trees(self) -> Sequence[_DecisionTreeModel]: ...
    @property
    def getNumTrees(self) -> int: ...
    @property
    def treeWeights(self) -> List[float]: ...
    @property
    def totalNumNodes(self) -> int: ...
    @property
    def toDebugString(self) -> str: ...

class _TreeEnsembleParams(_DecisionTreeParams):
    subsamplingRate: Param[float]
    supportedFeatureSubsetStrategies: List[str]
    featureSubsetStrategy: Param[str]
    def __init__(self) -> None: ...
    def getSubsamplingRate(self) -> float: ...
    def getFeatureSubsetStrategy(self) -> str: ...

class _RandomForestParams(_TreeEnsembleParams):
    numTrees: Param[int]
    def __init__(self) -> None: ...
    def getNumTrees(self) -> int: ...

class _GBTParams(_TreeEnsembleParams, HasMaxIter, HasStepSize, HasValidationIndicatorCol):
    stepSize: Param[float]
    validationTol: Param[float]
    def getValidationTol(self) -> float: ...

class _HasVarianceImpurity(Params):
    supportedImpurities: List[str]
    impurity: Param[str]
    def __init__(self) -> None: ...
    def getImpurity(self) -> str: ...

class _TreeClassifierParams:
    supportedImpurities: List[str]
    impurity: Param[str]
    def __init__(self) -> None: ...
    def getImpurity(self) -> str: ...

class _TreeRegressorParams(_HasVarianceImpurity): ...
