from astropy.io import fits

def fill_primary_header(d):
    p_hdr = fits.Header()
    p_hdr["HDRVER"]   = ('3.4             '   , "Header version                               ")
    p_hdr["FITSTYPE"] = ('PSRFITS'            , "FITS definition for pulsar data files        ")
    p_hdr["DATE"]     = ( d.file_date         , "File creation date (YYYY-MM-DDThh:mm:ss UTC) ")
    p_hdr["OBSERVER"] = ( d.observer          , "Observer name(s)                             ")
    p_hdr["PROJID"]   = ( d.proj_id           , "Project name                                 ")
    p_hdr["TELESCOP"] = ( d.telescope         , "Telescope name                               ")
    p_hdr["ANT_X"]    = ( d.ant_x             , "[m] Antenna ITRF X-coordinate (D)            ")
    p_hdr["ANT_Y"]    = ( d.ant_y             , "[m] Antenna ITRF Y-coordinate (D)            ")
    p_hdr["ANT_Z"]    = ( d.ant_z             , "[m] Antenna ITRF Z-coordinate (D)            ")
    p_hdr["FRONTEND"] = ('                '   , "Rx and feed ID                               ")
    p_hdr["NRCVR"]    = (1                    , "Number of receiver polarisation channels     ")
    p_hdr["FD_POLN"]  = ('CIRC'               , "LIN or CIRC                                  ")
    p_hdr["FD_HAND"]  = (-1                   , "+/- 1. +1 is LIN:A=X,B=Y, CIRC:A=L,B=R (I)   ")
    p_hdr["FD_SANG"]  = (45.0                 , "[deg] FA of E vect for equal sig in A&B (E)  ")
    p_hdr["FD_XYPH"]  = (0.0                  , "[deg] Phase of A^* B for injected cal (E)    ")
    p_hdr["BACKEND"]  = ('YUPPI'              , "Backend ID                                   ")
    p_hdr["BECONFIG"] = ('N/A'                , "Backend configuration file name              ")
    p_hdr["BE_PHASE"] = (-1                   , "0/+1/-1 BE cross-phase:0 unknown,+/-1 std/rev")
    p_hdr["BE_DCC"]   = (0                    , "0/1 BE downconversion conjugation corrected  ")
    p_hdr["BE_DELAY"] = (0.0                  , "[s] Backend propn delay from digitiser input ")
    p_hdr["TCYCLE"]   = (0.0                  , "[s] On-line cycle time (D)                   ")
    p_hdr["OBS_MODE"] = ('SEARCH'             , "(PSR, CAL, SEARCH)                           ")
    p_hdr["DATE-OBS"] = ( d.obs_date          , "Date of observation (YYYY-MM-DDThh:mm:ss UTC)")
    p_hdr["OBSFREQ"]  = ( d.fcenter           , "[MHz] Centre frequency for observation       ")
    p_hdr["OBSBW"]    = ( d.bw                , "[MHz] Bandwidth for observation              ")
    p_hdr["OBSNCHAN"] = ( d.nchan             , "Number of frequency channels (original)      ")
    p_hdr["CHAN_DM"]  = (                 0.0 , "DM used to de-disperse each channel (pc/cm^3)")
    p_hdr["SRC_NAME"] = ( d.src_name          , "Source or scan ID                            ")
    p_hdr["COORD_MD"] = ('J2000'              , "Coordinate mode (J2000, GAL, ECLIP, etc.)    ")
    p_hdr["EQUINOX"]  = (2000.0               , "Equinox of coords (e.g. 2000.0)              ")
    p_hdr["RA"]       = ( d.ra_str            , "Right ascension (hh:mm:ss.ssss)              ")
    p_hdr["DEC"]      = ( d.dec_str           , "Declination (-dd:mm:ss.sss)                  ")
    p_hdr["BMAJ"]     = ( d.bmaj_deg          , "[deg] Beam major axis length                 ")
    p_hdr["BMIN"]     = ( d.bmin_deg          , "[deg] Beam minor axis length                 ")
    p_hdr["BPA"]      = ( d.bpa_deg           , "[deg] Beam position angle                    ")
    p_hdr["STT_CRD1"] = ( d.ra_str            , "Start coord 1 (hh:mm:ss.sss or ddd.ddd)      ")
    p_hdr["STT_CRD2"] = ( d.dec_str           , "Start coord 2 (-dd:mm:ss.sss or -dd.ddd)     ")
    p_hdr["TRK_MODE"] = ('TRACK'              , "Track mode (TRACK, SCANGC, SCANLAT)          ")
    p_hdr["STP_CRD1"] = ( d.ra_str            , "Stop coord 1 (hh:mm:ss.sss or ddd.ddd)       ")
    p_hdr["STP_CRD2"] = ( d.dec_str           , "Stop coord 2 (-dd:mm:ss.sss or -dd.ddd)      ")
    p_hdr["SCANLEN"]  = ( d.scan_len          , "[s] Requested scan length (E)                ")
    p_hdr["FD_MODE"]  = ('FA'                 , "Feed track mode - FA, CPA, SPA, TPA          ")
    p_hdr["FA_REQ"]   = (0.0                  , "[deg] Feed/Posn angle requested (E)          ")
    p_hdr["CAL_MODE"] = ('OFF'                , "Cal mode (OFF, SYNC, EXT1, EXT2)             ")
    p_hdr["CAL_FREQ"] = (0.0                  , "[Hz] Cal modulation frequency (E)            ")
    p_hdr["CAL_DCYC"] = (0.0                  , "Cal duty cycle (E)                           ")
    p_hdr["CAL_PHS"]  = (0.0                  , "Cal phase (wrt start time) (E)               ")
    p_hdr["STT_IMJD"] = ( d.stt_imjd          , "Start MJD (UTC days) (J - long integer)      ")
    p_hdr["STT_SMJD"] = ( d.stt_smjd          , "[s] Start time (sec past UTC 00h) (J)        ")
    p_hdr["STT_OFFS"] = ( d.stt_offs          , "[s] Start time offset (D)                    ")
    p_hdr["STT_LST"]  = ( d.stt_lst           , "[s] Start LST (D)                            ")  
    return p_hdr


def fill_table_header(d):
    t_hdr = fits.Header()
    t_hdr["INT_TYPE"] = ('TIME'               , "Time axis (TIME, BINPHSPERI, BINLNGASC, etc)   ")
    t_hdr["INT_UNIT"] = ('SEC'                , "Unit of time axis (SEC, PHS (0-1), DEG)        ")
    t_hdr["SCALE"]    = ('FluxDen'            , "Intensity units (FluxDen/RefFlux/Jansky)       ")
    t_hdr["NPOL"]     = (1                    , "Nr of polarisations                            ")
    t_hdr["POL_TYPE"] = ('AA+BB'              , "Polarisation identifier (e.g., AABBCRCI, AA+BB)")
    t_hdr["TBIN"]     = ( d.dt                , "[s] Time per bin or sample                     ")
    t_hdr["NBIN"]     = (1                    , "Nr of bins (PSR/CAL mode; else 1)              ")
    t_hdr["NBIN_PRD"] = (0                    , "Nr of bins/pulse period (for gated data)       ")
    t_hdr["PHS_OFFS"] = (0.0                  , "Phase offset of bin 0 for gated data           ")
    t_hdr["NBITS"]    = ( d.nbits             , "Nr of bits/datum (SEARCH mode 'X' data, else 1)")
    t_hdr["NSUBOFFS"] = ( d.nsuboffs          , "Subint offset (Contiguous SEARCH-mode files)   ")
    t_hdr["NCHAN"]    = ( d.nchan             , "Number of channels/sub-bands in this file      ")
    t_hdr["CHAN_BW"]  = ( d.chan_bw           , "[MHz] Channel/sub-band width                   ") 
    t_hdr["NCHNOFFS"] = (0                    , "Channel/sub-band offset for split files        ")
    t_hdr["NSBLK"]    = ( d.nsblk             , "Samples/row (SEARCH mode, else 1)              ")
    return t_hdr
