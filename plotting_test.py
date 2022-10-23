from VectorField import VectorField
import cProfile
import pstats
import io

def main():
    vf = VectorField(None)
    vf.plot3dfield()

if __name__ == '__main__':
    cProfile.run('main()', 'profiling_results')
    s = io.StringIO()
    ps = pstats.Stats('profiling_results', stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())

