#!/usr/bin/env python

"""Run experiment with specified program with given compilers."""

import os
import subprocess as sp
import textwrap as tw
import collections as cl


def main():
    """Invoke all necessary builds and experiments."""
    Settings = cl.namedtuple('Settings', 
        'compiler base_opt program_name '
        'benchmark_root_dir benchmark_source_dir')
    settings = Settings(compiler='gcc', base_opt='-O3', 
        program_name='atax', 
        benchmark_root_dir='../data/sources/polybench-c-3.2',
        benchmark_source_dir='linear-algebra/kernels/atax')

    build_reference(settings)
    build_timed(settings)


def create_local_settings(settings):
    """Create local settings from global."""
    local_settings = dict()
    local_settings['program_source'] = '{program_name}.c'.format(
        **{'program_name': settings.program_name})
    local_settings.update(settings._asdict())
    return local_settings


def prepare_command_build_reference(settings):
    """Prepare command for building of reference version of benchmark."""
    command = tw.dedent("""
        {compiler} -O0 -I utilities -I {benchmark_source_dir} 
        utilities/polybench.c {benchmark_source_dir}/{program_source} 
        -DPOLYBENCH_DUMP_ARRAYS 
        -o ./bin/{program_name}_ref""").translate(None, '\n').format(
        **settings)
    return command


def prepare_command_build_timed(settings):
    """Prepare command for building of timed version of benchmark."""
    command = tw.dedent("""
        {compiler} {base_opt} -I utilities 
        -I {benchmark_source_dir} utilities/polybench.c 
        {benchmark_source_dir}/{program_source} -DPOLYBENCH_TIME 
        -o ./bin/{program_name}_time""").translate(None, '\n').format(
        **settings)
    return command


def prepare_command_run_reference(settings):
    """Prepare command for running the reference version of program."""
    command = tw.dedent("""
        ./bin/{program_name}_ref 1>./output/{program_name}_ref.out 
        2>./output/{program_name}_ref.err""").translate(None, '\n').format(
        **settings)
    return command


def prepare_command_run_timed(settings):
    """Prepare command for running the timed version of program."""
    command = tw.dedent("""
        ./bin/{program_name}_time 1>./output/{program_name}_time.out 
        2>./output/{program_name}_time.err""").translate(None, '\n').format(
        **settings)
    return command


def build_reference(settings):
    """Build the reference version of the benchmark."""
    local_settings = create_local_settings(settings)
    command = prepare_command_reference(local_settings)
    os.chdir(local_settings['benchmark_root_dir'])
    print os.path.realpath(os.path.curdir)
    print command
    raw_input()
    sp.call('mkdir bin'.split())
    sp.check_call(command.split())


def run_reference(settings):
    """Run the reference version of program."""
    command = prepare_command_reference(settings)
    sp.check_call(command.split())


def run_timed(settings):
    """Run the timed version of program."""
    command = prepare_command_timed(settings)
    sp.check_call(command.split())


def build_timed(settings):
    """Build the timed version of the benchmark."""
    local_settings = create_local_settings(settings)
    command = prepare_command_timed(local_settings)
    os.chdir(local_settings['benchmark_root_dir'])
    print os.path.realpath(os.path.curdir)
    print command
    raw_input()
    sp.call('mkdir bin'.split())
    sp.check_call(command.split())


if __name__ == '__main__':
    main()
