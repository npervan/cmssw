import FWCore.ParameterSet.Config as cms

from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer
laserTask = DQMEDAnalyzer(
	"LaserTask",
	
	#	standard parameters
	name       = cms.untracked.string("LaserTask"),
	debug      = cms.untracked.int32(0),
	runkeyVal  = cms.untracked.int32(0),
	runkeyName = cms.untracked.string("pp_run"),
	ptype      = cms.untracked.int32(0),
	mtype      = cms.untracked.bool(True),
	subsystem  = cms.untracked.string("HcalCalib"),

	#	tags
	tagHBHE     = cms.untracked.InputTag("hcalDigis"),
	tagHO       = cms.untracked.InputTag("hcalDigis"),
	tagHF       = cms.untracked.InputTag("hcalDigis"),
	taguMN      = cms.untracked.InputTag("hcalDigis"),
	tagRaw      = cms.untracked.InputTag('hltHcalCalibrationRaw'),
	tagLaserMon = cms.untracked.InputTag("LASERMON"),

	laserType = cms.untracked.uint32(0),

	nevents = cms.untracked.int32(10000),

	# laser mon stuff
	laserMonCBox = cms.untracked.int32(5),
	laserMonIEta = cms.untracked.int32(0),
	vLaserMonIPhi = cms.untracked.vint32(23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0),
	laserMonDigiOverlap = cms.untracked.int32(2), # digis have 6 TSes, but overlap by 2.
	laserMonTS0 = cms.untracked.int32(65), # Timing is set so the peak is in TS 69.
)
