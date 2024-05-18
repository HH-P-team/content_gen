import './Section.css';
import ActiveImage from '../ActiveImage/ActiveImage';

export default function Section(props) {
    return (
        <div className="Section">
            <div className='SectionHeader'>
                <div className='SectionHeaderImage'>
                    <ActiveImage message={props.name}/>
                </div>
                <div className='SectionTitle'>{props.name}</div>
            </div>
            <div className='SectionContent'>
            </div>
        </div>
    );
}
