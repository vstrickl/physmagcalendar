import React from 'react';
import ReactDOM from 'react-dom/client';
import FullCalendar from '@fullcalendar/react';
import timeGridPlugin from '@fullcalendar/timegrid';

const CalendarComponent = () => {
    const studio_id = window.studioCalendarId;
    const von_privates_id = window.vonsPrivatesId;

    console.log('Calendar IDs from window:', { studio_id, von_privates_id });

    return (
        <FullCalendar
            plugins={[timeGridPlugin]}
            initialView="timeGridWeek"
            headerToolbar={{
                left: 'prev',
                center: 'Martial Arts Studio',
                right: 'timeGridWeek,timeGridFourDay,timeGridDay,next'
            }}
            firstDay={1} // Set the first day of the week to Monday (0 = Sunday, 1 = Monday)
            slotMinTime="12:00:00" 
            events={(info, successCallback, failureCallback) => {
                if (!studio_id || !von_privates_id) {
                    console.error('Calendar IDs not found in window object');
                    failureCallback(new Error('Calendar IDs not configured'));
                    return;
                }
                
                Promise.all([
                    fetch(`/studio/api/calendar/${encodeURIComponent(studio_id)}/`),
                    fetch(`/studio/api/calendar/${encodeURIComponent(von_privates_id)}/`)
                ])
                .then(async responses => {
                    for (const response of responses) {
                        if (!response.ok) {
                            const text = await response.text();
                            console.error('Response not OK:', {
                                status: response.status,
                                statusText: response.statusText,
                                body: text
                            });
                            throw new Error(`HTTP error! status: ${response.status}`);
                        }
                    }
                    return Promise.all(responses.map(res => res.json()));
                })
                .then(([studioEvents, privateEvents]) => {
                    const formattedEvents = [
                        ...studioEvents.map(event => ({
                            title: event.summary,
                            start: event.start.dateTime || event.start.date,
                            end: event.end.dateTime || event.end.date,
                            description: event.description,
                            location: event.location,
                            source: 'studio',
                            color: '#D50000'  // Blue for studio events
                        })),
                        ...privateEvents.map(event => ({
                            title: event.summary,
                            start: event.start.dateTime || event.start.date,
                            end: event.end.dateTime || event.end.date,
                            description: event.description,
                            location: event.location,
                            source: 'private',
                            color: '#3F51B5'  // Green for private events
                        }))
                    ];
                    
                    console.log('Formatted events:', {
                        total: formattedEvents.length,
                        studio: formattedEvents.filter(e => e.source === 'studio').length,
                        private: formattedEvents.filter(e => e.source === 'private').length,
                        sampleStudio: formattedEvents.find(e => e.source === 'studio'),
                        samplePrivate: formattedEvents.find(e => e.source === 'private')
                    });

                    successCallback(formattedEvents);
                })
                .catch(error => {
                    console.error('Error fetching calendar events:', error);
                    failureCallback(error);
                });
            }}
        />
    );
};

const root = ReactDOM.createRoot(document.getElementById('react-calendar'));
root.render(<CalendarComponent />);