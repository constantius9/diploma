"""This module describes the data types (structures) used in rest of the 
system.
"""

Context = rt.recordtype('Context',
    'paths_stack settings')

SettingsBase = rt.recordtype('Settings', 
    'program_name benchmark_root_dir framework_root_dir '
    'build_settings run_settings benchmark_bin_dir')

class Settings(PrintableStructure, SettingsBase):
    pass


HardwareInfoBase = rt.recordtype('HardwareInfo',
    'cpu_mhz cache_size flags')

class HardwareInfo(PrintableStructure, HardwareInfoBase):
    pass


BuildSettingsBase = rt.recordtype('BuildSettings',
    'compiler base_opt optimization_flags other_flags '
    'benchmark_source_dir program_source linker_options')

class BuildSettings(PrintableStructure, BuildSettingsBase):
    pass


RunSettingsBase = rt.recordtype('RunSettings',
    '')

class RunSettings(PrintableStructure, RunSettingsBase):
    pass


Input = cl.namedtuple('Input',
    'benchmark_source_dir compiler base_opt')


CalibrationResultBase = cl.namedtuple('CalibrationResult',
    'total_time time dispersion variance runs_number times_list')

class CalibrationResult(PrintableStructure, CalibrationResultBase):
    pass


ValidationResultBase = cl.namedtuple('ValidationResult',
    'real_time measured_time error relative_error')

class ValidationResult(PrintableStructure, ValidationResultBase):
    pass