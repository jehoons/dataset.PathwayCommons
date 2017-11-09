from ipdb import set_trace
from os import system 
from os.path import dirname, join, basename 
import v9


def test_main(): 

    targetfiles = """
    pathways-sbgn.tar.gz
    paxtools.jar
    datasources.txt
    blacklist.txt
    pathways.txt.gz
    PathwayCommons9.wp.uniprot.gmt.gz
    PathwayCommons9.wp.hgnc.txt.gz
    PathwayCommons9.wp.hgnc.sif.gz
    PathwayCommons9.wp.hgnc.gmt.gz
    PathwayCommons9.wp.BIOPAX.owl.gz
    PathwayCommons9.Warehouse.BIOPAX.owl.gz
    PathwayCommons9.smpdb.uniprot.gmt.gz
    PathwayCommons9.smpdb.hgnc.txt.gz
    PathwayCommons9.smpdb.hgnc.sif.gz
    PathwayCommons9.smpdb.hgnc.gmt.gz
    PathwayCommons9.smpdb.BIOPAX.owl.gz
    PathwayCommons9.reconx.hgnc.txt.gz
    PathwayCommons9.reconx.hgnc.sif.gz
    PathwayCommons9.reconx.BIOPAX.owl.gz
    PathwayCommons9.reactome.uniprot.gmt.gz
    PathwayCommons9.reactome.hgnc.txt.gz
    PathwayCommons9.reactome.hgnc.sif.gz
    PathwayCommons9.reactome.hgnc.gmt.gz
    PathwayCommons9.reactome.BIOPAX.owl.gz
    PathwayCommons9.psp.hgnc.txt.gz
    PathwayCommons9.psp.hgnc.sif.gz
    PathwayCommons9.psp.BIOPAX.owl.gz
    PathwayCommons9.pid.uniprot.gmt.gz
    PathwayCommons9.pid.hgnc.txt.gz
    PathwayCommons9.pid.hgnc.sif.gz
    PathwayCommons9.pid.hgnc.gmt.gz
    PathwayCommons9.pid.BIOPAX.owl.gz
    PathwayCommons9.panther.uniprot.gmt.gz
    PathwayCommons9.panther.hgnc.txt.gz
    PathwayCommons9.panther.hgnc.sif.gz
    PathwayCommons9.panther.hgnc.gmt.gz
    PathwayCommons9.panther.BIOPAX.owl.gz
    PathwayCommons9.netpath.uniprot.gmt.gz
    PathwayCommons9.netpath.hgnc.txt.gz
    PathwayCommons9.netpath.hgnc.sif.gz
    PathwayCommons9.netpath.hgnc.gmt.gz
    PathwayCommons9.netpath.BIOPAX.owl.gz
    PathwayCommons9.msigdb.hgnc.txt.gz
    PathwayCommons9.msigdb.hgnc.sif.gz
    PathwayCommons9.msigdb.BIOPAX.owl.gz
    PathwayCommons9.mirtarbase.BIOPAX.owl.gz
    PathwayCommons9.kegg.uniprot.gmt.gz
    PathwayCommons9.kegg.hgnc.txt.gz
    PathwayCommons9.kegg.hgnc.sif.gz
    PathwayCommons9.kegg.hgnc.gmt.gz
    PathwayCommons9.kegg.BIOPAX.owl.gz
    PathwayCommons9.intact.hgnc.txt.gz
    PathwayCommons9.intact.hgnc.sif.gz
    PathwayCommons9.intact_complex.hgnc.txt.gz
    PathwayCommons9.intact_complex.hgnc.sif.gz
    PathwayCommons9.intact_complex.BIOPAX.owl.gz
    PathwayCommons9.intact.BIOPAX.owl.gz
    PathwayCommons9.inoh.uniprot.gmt.gz
    PathwayCommons9.inoh.hgnc.txt.gz
    PathwayCommons9.inoh.hgnc.sif.gz
    PathwayCommons9.inoh.hgnc.gmt.gz
    PathwayCommons9.inoh.BIOPAX.owl.gz
    PathwayCommons9.humancyc.uniprot.gmt.gz
    PathwayCommons9.humancyc.hgnc.txt.gz
    PathwayCommons9.humancyc.hgnc.sif.gz
    PathwayCommons9.humancyc.hgnc.gmt.gz
    PathwayCommons9.humancyc.BIOPAX.owl.gz
    PathwayCommons9.hprd.hgnc.txt.gz
    PathwayCommons9.hprd.hgnc.sif.gz
    PathwayCommons9.hprd.BIOPAX.owl.gz
    PathwayCommons9.drugbank.hgnc.txt.gz
    PathwayCommons9.drugbank.hgnc.sif.gz
    PathwayCommons9.drugbank.BIOPAX.owl.gz
    PathwayCommons9.dip.hgnc.txt.gz
    PathwayCommons9.dip.hgnc.sif.gz
    PathwayCommons9.dip.BIOPAX.owl.gz
    PathwayCommons9.Detailed.uniprot.gmt.gz
    PathwayCommons9.Detailed.hgnc.txt.gz
    PathwayCommons9.Detailed.hgnc.sif.gz
    PathwayCommons9.Detailed.hgnc.gmt.gz
    PathwayCommons9.Detailed.BIOPAX.owl.gz
    PathwayCommons9.ctd.hgnc.txt.gz
    PathwayCommons9.ctd.hgnc.sif.gz
    PathwayCommons9.ctd.BIOPAX.owl.gz
    PathwayCommons9.corum.hgnc.txt.gz
    PathwayCommons9.corum.hgnc.sif.gz
    PathwayCommons9.corum.BIOPAX.owl.gz
    PathwayCommons9.biogrid.hgnc.txt.gz
    PathwayCommons9.biogrid.hgnc.sif.gz
    PathwayCommons9.biogrid.BIOPAX.owl.gz
    PathwayCommons9.bind.hgnc.txt.gz
    PathwayCommons9.bind.hgnc.sif.gz
    PathwayCommons9.bind.BIOPAX.owl.gz
    PathwayCommons9.All.uniprot.gmt.gz
    PathwayCommons9.All.hgnc.txt.gz
    PathwayCommons9.All.hgnc.sif.gz
    PathwayCommons9.All.hgnc.gmt.gz
    PathwayCommons9.All.BIOPAX.owl.gz
    export.sh.gz
    """

    targetfiles = targetfiles.split('\n')
    targetfiles = [x.strip() for x in targetfiles]
    targetfiles = list(filter(lambda x: len(x) > 0, targetfiles))
    baseurl = 'http://www.pathwaycommons.org/archives/PC2/v9'

    for afile in targetfiles: 
        filedir = dirname(v9.__file__)
        savefile = join(filedir, basename(afile))
        cmd = 'wget -q --show-progress %s/%s -O %s' % (baseurl, afile, savefile)  
        system(cmd)

    # set_trace()
    assert True 


