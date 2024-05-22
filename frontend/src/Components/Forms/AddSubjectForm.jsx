import './AddSubjectForm.css';
import { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { createSubject } from '../../api/subjects/subject.api';
import Button from '../Button/Button';

export default function AddSubjectForm(props) {

    const [subjectName, setSubjectName] = useState('')
    const dispatch = useDispatch();
    const visibleMenu = useSelector((state) => state.addSubjectMenuState)

    const handleSubmit = (e, subjectName) => {
        
        dispatch({ type: 'CASE_SUBJECT_MENUSTATE', value: !visibleMenu })

        createSubject(subjectName).then((data) => {
            if (data.status) {
                dispatch({ type: 'CASE_ADD_SUBJECTS', value: [data.result] })
            }
        })
        setSubjectName('');
        e.preventDefault();
    };

    const handleInput = (e) => {
        setSubjectName(e.target.value);
        e.preventDefault();
    }

    const handleCkick = () => {
        dispatch({ type: 'CASE_SUBJECT_MENUSTATE', value: !visibleMenu })
    }

    if (visibleMenu) {
        return (
            <div>
                <form className='AddSubjectForm' onSubmit={(e) => handleSubmit(e, subjectName)}>
                    <div className='InputWrapper'>
                        <input 
                            className={'FormInput'} 
                            name={'input'}
                            value={subjectName} 
                            onInput={handleInput} 
                            placeholder={'Введите...'}
                        />
                    </div>
                    <button className={'Button'} type="submit">OK</button>
                </form> 
            </div>
        );
    } else {
        return (<Button name={'Добавить'} action={handleCkick}/>)
    }
}
