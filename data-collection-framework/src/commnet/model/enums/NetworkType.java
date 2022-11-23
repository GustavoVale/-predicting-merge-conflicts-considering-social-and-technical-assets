package commnet.model.enums;

public enum NetworkType {
	ALL ("A"),
	NETWORKS ("N"),
	CONTCOMNETWORKS ("CCN"),
	CONTRIBUTIONNETWORKS ("CONTN"),
	COMPREHENSIVENETWORKS ("COMPN"),
	PRECISENETWORKS ("PREN"),
	CHANGEDARTIFACTNETWORKS ("ARTN"),
	COMMUNICATIONNETWORKS ("COMN"),
	MERGESCENARIO ("MS"),
	ISSUE ("I"),
	ALLMETRICS ("MA"),
	PROJECTMETRICS ("MP"),
	NETWORKMETRICS ("MN"),
	MERGEMETRICS ("MM"),
	FILEMETRICS ("MF"),
	CHUNKMETRICS ("MC"),
	COMPREHENSIVECOMMUNICATORS ("CCOMM"),
	PRECISECOMMUNICATORS ("PCOMM"),
	CHANGEDARTIFACTCOMMUNICATORS ("ACOMM"),
	DEVS ("D"),
	COMMITTERS ("C"),
	INTEGRATORS ("IT"),
	MERGECONFLICTINFO ("MCI"),
	MERGECONFLICTMETRICS ("MCM");
	
	String description;

	NetworkType (String desc){
		this.description = desc;
	}
	
	@Override
	public String toString(){
		return description;
	}
}
